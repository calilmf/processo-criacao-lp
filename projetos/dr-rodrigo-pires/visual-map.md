# Mapa Visual — Dr. Rodrigo Pires

## Direção geral

- **Tom visual:** editorial-clínico técnico. Menos "acolhedor caloroso" (que é o tom do Dr. Gustavo), mais "cirurgião preciso + médico esportivo". Diferenciação intencional de identidade dentro da mesma agência.
- **Densidade:** média para baixa — respiro editorial nas seções internas, hero mais denso com prova imediata.
- **Tipo de imagem:** foto do médico em consultório (plano médio, olhando para câmera), fundo de consultório desfocado. Sem stock. Sem antes/depois. Sem paciente identificável.
- **Iconografia:** ícones em 6 cards de serviços, um por card. Processo completo em `mapa-icones.md`: `cards.json` → `harvest-candidatos.py` (67 candidatos baixados) → `contact-sheet.py` (revisão visual) → seleção a 32px. Todos bucket A. Arquivos em `assets/topic-icons/rodrigo-pires/`. Cards de "Quando procurar" e "Abordagem" **sem ícones** por decisão — funcionam melhor em tipografia pura.
- **Movimento e microinterações:** nenhuma animação. Scroll natural. `<details>` nativo no FAQ (sem accordion custom).
- **Regra do CTA:** preservar verbo ("Agendar avaliação"), destino (WhatsApp via bridge), prioridade (único CTA primário por viewport) e tracking (`whatsapp_click` no dataLayer) definidos no briefing.

## Tokens — decisão de reuso vs override

Base: `assets/tokens.css` (Manrope + paleta ink/paper/teal/dark/sand/green).

**Overrides justificados:**

| Token | Base | LP Rodrigo | Justificativa |
| --- | --- | --- | --- |
| `--accent` (novo, mapeia CTA) | `--green #1f7a4d` | `--teal #254d55` (do próprio tokens.css) | Dr. Gustavo já ocupa acento burgundy warm. Reutilizar o `--teal` que já existe no tokens.css como cor primária dá identidade "cirúrgica sóbria" diferente sem inventar cor nova. Mantém coerência de agência. |
| `--paper` | `#f6f3ee` (cream warm) | `#f4f4f2` (paper neutro mais frio) | Tom cream é do Dr. Gustavo. Neutro frio empurra pro tom clínico-esportivo do Rodrigo. Delta pequeno de saturação — mesma família visual, diferente identidade. |
| Todo o resto (ink, muted, radius, fs-*, container, sombras) | — | mantido | Sem justificativa para mudar. |

Todos os outros tokens (tipografia, escala tipográfica, radius 8, container 1120, escala de heading, botão base) vêm de `assets/tokens.css` sem alteração.

## Referências do repertório

Cartões consultados em `visual-repertorio/03-cartoes-referencia/`:

| Seção | Função | Referências | Padrão aplicado | Decisão de interface | Risco a evitar |
| --- | --- | --- | --- | --- | --- |
| Hero | Contexto + ação inicial | `ref.visual.linear.hero-editorial-serifado` (dark, restrained, oversized) | Dark hero editorial com paper como transição | Fundo `--dark` com titulo oversized `clamp(40px,6vw,68px)`, CRM/RQE em pill próximo ao título (gate saude), CTA `--teal` alto contraste, foto do médico compondo à direita (desktop) ou abaixo (mobile) | Hero muito minimalista escondendo identificação profissional viola `saude.md` gate 1 — CRM/RQE fica visível no primeiro viewport |
| Prova rápida | Sinais imediatos | `ref.visual.stripe.narrativa-clara-espacosa` | Grid horizontal de 4 pills com institutos/formações | Pills em card branco com borda `--line`, radius 8, texto curto | Genérico se as pills forem vagas — cada uma precisa ser evidência específica (HBDF, Ceilândia EC, SBCJ, pós-grad) |
| Quando procurar | Reconhecimento da situação | `ref.visual.stripe.narrativa-clara-espacosa` | Two-column head (título grande + apoio) + lista de situações em card único | Card único com lista tipográfica, sem ícones por card (v1) | Cards separados por situação viraria "colônia de cards genéricos" — lista consolidada mantém foco |
| Abordagem | Mecanismo em 3 passos | `ref.visual.stripe.narrativa-clara-espacosa` | Steps numerados horizontais (desktop) / verticais (mobile) | Cards com número em `--teal`, título e apoio, sem ícone | Steps podem virar "receita padrão" — copy anti-promessa ("conservador primeiro, cirurgia quando o quadro pede") mantém peso clínico |
| Autoridade | Formação + foto | `ref.visual.forward.saude-humana-clara` (elementos: foto real, CRM/RQE em subtitulo, sem infantilizar) | Two-column: foto do médico + bloco de credenciais em lista | Foto real (plano médio no consultório), lista de credenciais em card, CRM/RQE em destaque | Foto de banco quebra tudo (spec saude) — se não houver foto real disponível, remover a coluna de foto e usar autoridade só textual |
| Serviços | O que a consulta cobre | `ref.visual.stripe.narrativa-clara-espacosa` + ícones bucket A | Grid 3x2 de cards leves. Cada card com ícone 28px em quadrado 48px `--accent-soft` no topo. Ícones renderizados em `--accent` para contraste sóbrio | Descrever "resultado" viola saude — só descrever o que é feito, "quando indicado" |
| Convênios | Prova comercial + positioning "servidor público federal" | Grid pill lista, sóbrio | Grid `repeat(6, 1fr)` no desktop, `repeat(3, 1fr)` tablet, `repeat(2, 1fr)` mobile. 30 convênios em pills. Fundo branco, pills em `--paper` | Se lista fica muito genérica sem hierarquia, ganha peso. Título posiciona explicitamente ("Cobertura ampla para servidor público federal") transforma a lista em diferencial, não só ornamento. |
| FAQ | Objeções | `ref.visual.notion.faq-progressivo-limpo` | `<details>` nativo | Zero JS, zero animação custom — o browser resolve | FAQ com perguntas de SEO em vez de objeções reais — cada pergunta cobre uma objeção do briefing |
| CTA final | Ação | Bridge page pattern (padrão Pulso) | Bloco final centralizado com fundo `--dark` e CTA `--teal` | Reforça CRM/RQE + endereços das unidades | Sem canal direto exposto no rodapé (regra `google-ads.md` §CTA) |

## Restrições que carregam para o build

- **Setor saúde (`specs/saude.md`):** identificação profissional no primeiro viewport, sem promessa/superlativo/promoção, sem foto de paciente, ícones seguindo `repertorio-icones.md` (v2: 6 ícones bucket A, contact sheet arquivado, ver `mapa-icones.md`).
- **Google Ads (`specs/google-ads.md`):** rodapé sem canal direto, CTA único por viewport, bridge page com evento antes do wa.me, política de privacidade linkada. Consent Mode v2 e GTM entram na versão que for pra produção — este preview no GitHub Pages fica com `noindex` (pra não indexar preview) e sem GTM (nada de tracking em ambiente de validação visual).
- **Base tipografia/token:** Manrope + tokens.css. Overrides listados acima, justificados. Nada mais.
