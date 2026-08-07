# Mapa Visual — Dr. Rodrigo Pires

## Direção geral

- **Tom visual (v2, puxado do site real):** editorial premium warm-clínico — paleta navy profundo + dourado + creme herdada de `https://drrodrigopires.com.br/` (inspecionada com Playwright). Menos "cirurgião técnico frio", mais "consultório premium com peso institucional". Continua distinto do Dr. Gustavo (que usa burgundy/cream warm) por conta do dourado editorial (não terracota) e do navy (não dark quase preto).
- **Densidade:** média para baixa — respiro editorial nas seções internas, hero mais denso com prova imediata.
- **Tipo de imagem:** retrato do médico no hero (plano médio, olhando para câmera, fundo warm-tostado). **Autoridade usa foto do consultório real, não o retrato** — retrato do médico não se repete na página (regra `docs/uso-de-fotos.md`, incidente PR #9). Sem stock. Sem antes/depois. Sem paciente identificável.
- **Iconografia:** ícones em 6 cards de serviços, um por card. Processo completo em `mapa-icones.md`. **Recoloreados em `#d4b589` (gold)** via Iconify API na v2 pra casar com identidade do site — não usam mais o `--accent` (navy) como fill. Cards de "Quando procurar" e "Abordagem" **sem ícones** por decisão — funcionam melhor em tipografia pura.
- **Movimento e microinterações:** nenhuma animação. Scroll natural. `<details>` nativo no FAQ (sem accordion custom).
- **Regra do CTA:** preservar verbo ("Agendar avaliação"), destino (WhatsApp via bridge), prioridade (único CTA primário por viewport) e tracking (`whatsapp_click` no dataLayer) definidos no briefing. Primary button ganhou ícone WhatsApp inline (SVG 2-path) — herdado do padrão de conversão do próprio site do cliente.

## Tokens — v2 puxada do site real

**Mudança importante em relação à v1:** os tokens não vêm mais de `assets/tokens.css` puros — a LP virou uma sobrescrita quase completa via `:root` no próprio `previews/dr-rodrigo-pires.html`. Motivo: a v1 usando tokens base (Manrope + paper neutro + teal) ficou visualmente irmã de outras entregas recentes (feedback direto do cliente: "está praticamente idêntico ao Dr. Matheus Cavalcanti"). A correção foi inspecionar `drrodrigopires.com.br` com Playwright e puxar paleta, tipografia e tratamento dele.

**Tokens da v2 (todos aplicados via `:root` na própria página):**

| Token | Valor | Origem |
| --- | --- | --- |
| `--navy` / `--ink` | `#212e51` | Cor principal do site (headings, body text, CTA primary) |
| `--navy-dark` | `#1a2440` | Gradiente do CTA final |
| `--gold` | `#d4b589` | Cor secundária do site (kickers, accents, ícones) |
| `--gold-strong` | `#b89762` | Kicker em uppercase, list markers, hover |
| `--gold-soft` | `rgba(212,181,137,0.14)` | Fundo do quadrado do ícone dos cards |
| `--paper` | `#f3ebde` | Cream do hero e footer do site |
| `--paper-deep` | `#ebe0cc` | Gradiente do hero |
| `--font-sans` | `"Montserrat", ...` | Tipografia do site (era Manrope na v1) |
| `--radius-pill` | `30px` | Pill dos botões do site |
| `--shadow-cta` | `0 4px 10px rgba(0,0,0,0.22)` | Sombra do CTA primary do site |
| Headings | `text-transform: capitalize` | Padrão de Title Case Por Palavra do site (v1 usava caixa mista) |

**Elementos adicionais:**
- Botão primary: pill navy + peso 600 + ícone WhatsApp SVG inline.
- Botão ghost: transparente + texto navy + borda `1.6px` gold.
- `.card .card-icon`: 52×52 arredondado 999px, fundo `--gold-soft`, borda gold 0.35 opacidade.
- `.step-num`: 36×36 navy circle com número em gold.
- Todos os accents de lista, dots e borders internas: `--gold-strong`.
- CTA final: gradiente navy→navy-dark com kicker gold, primary button vira branco+navy+ícone WhatsApp.

Ou seja: `assets/tokens.css` não foi editado, mas a LP praticamente não o usa mais para cor. Continua herdando apenas escala tipográfica e container width (que ficaram compatíveis).

## Referências do repertório

Cartões consultados em `visual-repertorio/03-cartoes-referencia/`:

| Seção | Função | Referências | Padrão aplicado | Decisão de interface | Risco a evitar |
| --- | --- | --- | --- | --- | --- |
| Hero | Contexto + ação inicial | `ref.visual.linear.hero-editorial-serifado` (dark, restrained, oversized) | Dark hero editorial com paper como transição | Fundo `--dark` com titulo oversized `clamp(40px,6vw,68px)`, CRM/RQE em pill próximo ao título (gate saude), CTA `--teal` alto contraste, foto do médico compondo à direita (desktop) ou abaixo (mobile) | Hero muito minimalista escondendo identificação profissional viola `saude.md` gate 1 — CRM/RQE fica visível no primeiro viewport |
| Prova rápida | Sinais imediatos | `ref.visual.stripe.narrativa-clara-espacosa` | Grid horizontal de 4 pills com institutos/formações | Pills em card branco com borda `--line`, radius 8, texto curto | Genérico se as pills forem vagas — cada uma precisa ser evidência específica (HBDF, Ceilândia EC, SBCJ, pós-grad) |
| Quando procurar | Reconhecimento da situação | `ref.visual.stripe.narrativa-clara-espacosa` | Two-column head (título grande + apoio) + lista de situações em card único | Card único com lista tipográfica, sem ícones por card (v1) | Cards separados por situação viraria "colônia de cards genéricos" — lista consolidada mantém foco |
| Abordagem | Mecanismo em 3 passos | `ref.visual.stripe.narrativa-clara-espacosa` | Steps numerados horizontais (desktop) / verticais (mobile) | Cards com número em `--teal`, título e apoio, sem ícone | Steps podem virar "receita padrão" — copy anti-promessa ("conservador primeiro, cirurgia quando o quadro pede") mantém peso clínico |
| Autoridade | Formação + prova de ambiente | `ref.visual.forward.saude-humana-clara` (elementos: foto real, CRM/RQE em subtitulo, sem infantilizar) | Two-column: foto do consultório real + bloco de credenciais em lista | Foto do consultório real (não do médico — o retrato já está no hero, repetir seria redundante e cansativo), lista de credenciais em card, CRM/RQE em destaque | Foto de banco quebra tudo (spec saude); repetir o retrato do médico duas vezes na mesma página cansa e enfraquece o hero — usar foto do ambiente é prova adicional legítima |
| Serviços | O que a consulta cobre | `ref.visual.stripe.narrativa-clara-espacosa` + ícones bucket A | Grid 3x2 de cards leves. Cada card com ícone 28px em quadrado 48px `--accent-soft` no topo. Ícones renderizados em `--accent` para contraste sóbrio | Descrever "resultado" viola saude — só descrever o que é feito, "quando indicado" |
| Convênios | Prova comercial + positioning "servidor público federal" | Grid pill lista, sóbrio | Grid `repeat(6, 1fr)` no desktop, `repeat(3, 1fr)` tablet, `repeat(2, 1fr)` mobile. 30 convênios em pills. Fundo branco, pills em `--paper` | Se lista fica muito genérica sem hierarquia, ganha peso. Título posiciona explicitamente ("Cobertura ampla para servidor público federal") transforma a lista em diferencial, não só ornamento. |
| FAQ | Objeções | `ref.visual.notion.faq-progressivo-limpo` | `<details>` nativo | Zero JS, zero animação custom — o browser resolve | FAQ com perguntas de SEO em vez de objeções reais — cada pergunta cobre uma objeção do briefing |
| CTA final | Ação | Bridge page pattern (padrão Pulso) | Bloco final centralizado com fundo `--dark` e CTA `--teal` | Reforça CRM/RQE + endereços das unidades | Sem canal direto exposto no rodapé (regra `google-ads.md` §CTA) |

## Restrições que carregam para o build

- **Setor saúde (`specs/saude.md`):** identificação profissional no primeiro viewport, sem promessa/superlativo/promoção, sem foto de paciente, ícones seguindo `repertorio-icones.md` (v2: 6 ícones bucket A, contact sheet arquivado, ver `mapa-icones.md`).
- **Google Ads (`specs/google-ads.md`):** rodapé sem canal direto, CTA único por viewport, bridge page com evento antes do wa.me, política de privacidade linkada. Consent Mode v2 e GTM entram na versão que for pra produção — este preview no GitHub Pages fica com `noindex` (pra não indexar preview) e sem GTM (nada de tracking em ambiente de validação visual).
- **Base tipografia/token:** Montserrat (Google Fonts) + `:root` local com paleta navy/gold/cream extraída do site do cliente. `assets/tokens.css` continua carregado mas praticamente sem uso de cor nesta LP.

## Puxado do site do cliente

Seção exigida pelo `docs/checklists.md` (Design): registrar explicitamente o que foi observado no site atual do cliente e o que a LP puxou de lá.

**Site inspecionado:** `https://drrodrigopires.com.br/` (via Playwright, com `getComputedStyle` nos elementos principais).

| Observado no site | Puxado pra LP |
| --- | --- |
| Navy `#212e51` como cor principal (headings, body, CTA) | Adotado como `--navy` / `--ink` / cor primária de heading e CTA |
| Dourado `#d4b589` como acento consistente (kicker, borda, hover) | Adotado como `--gold`, aplicado em kicker/border/list markers/ícones |
| Cream do hero (bg quente `#f3ebde` degradando pra `#ebe0cc`) | Adotado como `--paper` / `--paper-deep`, aplicado em hero e footer |
| Montserrat + Title Case Por Palavra nas headings | Adotado — Google Fonts + `text-transform: capitalize` em h1/h2/h3 |
| CTA em pill (radius 30) + shadow `rgba(0,0,0,0.22) 0 4px 10px` | Adotado como `--radius-pill` + `--shadow-cta` |
| Foto do médico em fundo warm-tostado, plano médio | Mesma foto usada no hero, casa com o cream sem processamento extra |

**Não puxado (decisão consciente):**
- Copy "eliminar suas dores" do site em produção — viola `specs/saude.md` (promessa absoluta). LP mantém tom técnico-sóbrio próprio.
- Layout de blocos horizontais do site — a LP tem estrutura mais editorial (hero+prova+quando+abordagem+cards+autoridade+convênios+locais+FAQ+CTA) porque cumpre função de conversão, não de portfolio.

**Por que essa seção existe:** o aprendizado central do rework v1→v2. Sem essa inspeção, a LP vira genérica e homogeneizada com outras entregas da agência (aconteceu na v1: "praticamente idêntica ao Dr. Matheus Cavalcanti"). Regra promovida ao processo geral em `docs/processo-de-criacao.md` §4.1.
