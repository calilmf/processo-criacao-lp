"""Baixa CANDIDATOS de icone por card, de toda a base do Iconify, para escolha visual.

Existe por causa de uma falha real: icones foram escolhidos lendo o NOME numa
lista de texto, sem nunca renderizar. Ex.: "joints-outline" (que desenha um
JOELHO) foi parar num card "Articulacoes da coluna".

O conserto nao e "procurar melhor por nome" -- e ver varios candidatos
renderizados lado a lado e escolher olhando. Este script produz os candidatos;
o contact-sheet.py renderiza; a escolha e feita olhando.

Uso:
    python3 harvest-candidatos.py cards.json -o candidatos/

    cards.json:
    {
      "regiao": {
        "chave-do-card": {"titulo": "...", "termos": ["spine", "back pain"]}
      }
    }
"""

import argparse
import json
import os
import time
import urllib.parse
import urllib.request

API = "https://api.iconify.design"

# A API rejeita o User-Agent padrao do urllib com 403.
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
    )
}


def _abrir(url, timeout=20):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout)

# Sets multicoloridos / emoji / marca: nao servem para icone de card monocromatico.
SETS_BLOQUEADOS = {
    "noto", "noto-v1", "twemoji", "openmoji", "emojione", "emojione-v1",
    "emojione-monotone", "fluent-emoji", "fluent-emoji-flat",
    "fluent-emoji-high-contrast", "fxemoji", "streamline-color",
    "streamline-flex-color", "streamline-sharp-color", "streamline-ultimate-color",
    "streamline-freehand-color", "skill-icons", "logos", "simple-icons",
    "devicon", "vscode-icons", "flat-color-icons", "flagpack", "circle-flags",
    "cif", "flag", "cryptocurrency-color", "token-branded", "arcticons",
    "material-icon-theme", "catppuccin", "unjs", "pixel", "pinhead", "glyphs-poly",
}

# Preferencia: sets com vocabulario clinico/anatomico real primeiro.
PRIORIDADE = [
    "healthicons", "medical-icon", "streamline-ultimate", "streamline",
    "game-icons", "material-symbols", "hugeicons", "solar", "tabler",
    "iconoir", "ph", "mdi", "lucide", "carbon", "fluent",
]


def buscar(termo, limit=32):
    url = f"{API}/search?query={urllib.parse.quote(termo)}&limit={limit}"
    try:
        with _abrir(url) as r:
            return json.load(r).get("icons", [])
    except Exception as e:
        print(f"    ! busca '{termo}' falhou: {e}")
        return []


def pontuar(nome):
    """Menor = melhor. Prioriza set clinico e variante de contorno."""
    prefixo = nome.split(":")[0]
    p = PRIORIDADE.index(prefixo) if prefixo in PRIORIDADE else len(PRIORIDADE)
    slug = nome.split(":", 1)[1] if ":" in nome else nome
    # variantes de contorno primeiro; evitar duplicatas -24px/-alt
    contorno = 0 if ("outline" in slug or "line" in slug) else 1
    ruido = 1 if ("24px" in slug or slug.endswith("-alt")) else 0
    return (p, contorno, ruido, len(slug))


def baixar(nome, destino, cor="%23527d8f"):
    prefixo, slug = nome.split(":", 1)
    url = f"{API}/{prefixo}/{slug}.svg?color={cor}&width=32&height=32"
    try:
        with _abrir(url) as r:
            dados = r.read()
        if b"<svg" not in dados:
            return False
        with open(destino, "wb") as fh:
            fh.write(dados)
        return True
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cards")
    ap.add_argument("-o", "--saida", default="candidatos")
    ap.add_argument("-n", "--por-card", type=int, default=10)
    args = ap.parse_args()

    with open(args.cards, encoding="utf-8") as fh:
        cards = json.load(fh)

    total = 0
    for regiao, mapa in cards.items():
        for chave, info in mapa.items():
            vistos = []
            for termo in info["termos"]:
                for nome in buscar(termo):
                    prefixo = nome.split(":")[0]
                    if prefixo in SETS_BLOQUEADOS:
                        continue
                    if nome not in vistos:
                        vistos.append(nome)
                time.sleep(0.05)

            vistos.sort(key=pontuar)
            escolhidos = vistos[: args.por_card]

            pasta = os.path.join(args.saida, regiao, chave)
            os.makedirs(pasta, exist_ok=True)
            ok = 0
            for i, nome in enumerate(escolhidos):
                arq = f"{i:02d}_{nome.replace(':', '__')}.svg"
                if baixar(nome, os.path.join(pasta, arq)):
                    ok += 1
                    total += 1
            print(f"  {regiao}/{chave}: {ok} candidatos ({len(vistos)} achados)")

    print(f"\n{total} candidatos em {args.saida}/")
    print("Agora rode o contact-sheet.py e ESCOLHA OLHANDO.")


if __name__ == "__main__":
    main()
