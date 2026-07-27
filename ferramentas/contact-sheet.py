"""Gera um contact sheet HTML para revisao VISUAL obrigatoria de icones.

Esta ferramenta existe por causa de uma falha real: icones foram escolhidos
lendo o NOME numa lista de texto, sem nunca renderizar o desenho. Resultado,
entre outros: um icone chamado "joints-outline" (que desenha um JOELHO) foi
parar num card "Articulacoes da coluna". Nenhuma revisao textual pega isso.

Regra do processo: nenhum icone e aprovado sem ter passado por este contact
sheet. Criterio, por icone -- olhando SO o desenho, sem ler o titulo, da pra
dizer que parte do corpo/orgao e e qual e o problema?

Uso:
    python3 contact-sheet.py <pasta-de-icones> [-o saida.html] [--titulos t.json]

    <pasta-de-icones>  pasta com .svg (varre subpastas; cada subpasta vira secao)
    --titulos          json opcional {"nome-do-arquivo": "Titulo do card"}
                       para revisar o icone ao lado do texto que ele acompanha
"""

import argparse
import base64
import json
import os
import sys

TEMPLATE_HEAD = """<!doctype html>
<meta charset="utf-8">
<title>Contact sheet de icones</title>
<style>
  body { font-family: -apple-system, system-ui, sans-serif; background: #f5f4f0;
         color: #303235; margin: 0; padding: 32px; }
  h1 { font-size: 20px; margin: 0 0 4px; }
  .sub { color: #6b7280; font-size: 13px; margin-bottom: 28px; max-width: 60ch;
         line-height: 1.5; }
  h2 { font-size: 15px; text-transform: uppercase; letter-spacing: .08em;
       color: #53686a; margin: 32px 0 12px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
          gap: 14px; }
  .card { background: #fff; border: 1px solid rgba(83,104,106,.14);
          border-radius: 12px; padding: 16px; }
  .row { display: flex; align-items: center; gap: 16px; }
  .big { width: 96px; height: 96px; flex: none; }
  .real { width: 32px; height: 32px; flex: none; }
  .real-wrap { display:flex; flex-direction:column; align-items:center; gap:4px; }
  .tag { font-size: 9px; color: #9aa3a5; }
  .title { font-weight: 700; font-size: 14px; margin-top: 12px; }
  .file { font-size: 11px; color: #9aa3a5; margin-top: 2px;
          font-family: ui-monospace, monospace; word-break: break-all; }
</style>
<h1>Contact sheet de icones</h1>
<div class="sub">Criterio: olhando <b>so o desenho</b>, sem ler o titulo, da pra dizer
que parte do corpo/orgao e e qual e o problema? Se nao, redesenhar.
O quadrado pequeno e o tamanho real de uso (32px) &mdash; e nele que a legibilidade
precisa funcionar.</div>
"""


def collect(root):
    """Retorna {secao: [(caminho, nome)]} varrendo subpastas."""
    sections = {}
    for dirpath, _dirnames, filenames in os.walk(root):
        svgs = sorted(f for f in filenames if f.endswith(".svg"))
        if not svgs:
            continue
        rel = os.path.relpath(dirpath, root)
        section = "." if rel == "." else rel
        sections[section] = [(os.path.join(dirpath, f), f) for f in svgs]
    return dict(sorted(sections.items()))


def render(sections, titles):
    parts = [TEMPLATE_HEAD]
    total = 0
    for section, files in sections.items():
        label = section if section != "." else "(raiz)"
        parts.append(f'<h2>{label} &mdash; {len(files)} icones</h2>\n<div class="grid">')
        for path, name in files:
            with open(path, "rb") as fh:
                b64 = base64.b64encode(fh.read()).decode()
            src = f"data:image/svg+xml;base64,{b64}"
            stem = os.path.splitext(name)[0]
            title = titles.get(stem) or titles.get(name) or ""
            parts.append(
                '<div class="card"><div class="row">'
                f'<img class="big" src="{src}" alt="">'
                '<div class="real-wrap">'
                f'<img class="real" src="{src}" alt="">'
                '<span class="tag">32px</span>'
                "</div></div>"
                + (f'<div class="title">{title}</div>' if title else "")
                + f'<div class="file">{name}</div></div>'
            )
            total += 1
        parts.append("</div>")
    parts.append(f'<div class="sub" style="margin-top:32px">Total: {total} icones.</div>')
    return "\n".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pasta")
    ap.add_argument("-o", "--saida", default="contact-sheet.html")
    ap.add_argument("--titulos", help="json {arquivo: titulo do card}")
    args = ap.parse_args()

    if not os.path.isdir(args.pasta):
        sys.exit(f"pasta nao encontrada: {args.pasta}")

    titles = {}
    if args.titulos:
        with open(args.titulos, encoding="utf-8") as fh:
            titles = json.load(fh)

    sections = collect(args.pasta)
    if not sections:
        sys.exit(f"nenhum .svg encontrado em {args.pasta}")

    html = render(sections, titles)
    with open(args.saida, "w", encoding="utf-8") as fh:
        fh.write(html)

    n = sum(len(v) for v in sections.values())
    print(f"contact sheet com {n} icones -> {args.saida}")
    print("ABRA E OLHE antes de aprovar qualquer icone.")


if __name__ == "__main__":
    main()
