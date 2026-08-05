# Checklist de Entrega — Dr. Rodrigo Pires

Rodado sobre `previews/dr-rodrigo-pires.html` publicado no GitHub Pages.

## Estrategia

- [x] Promessa, prova e CTA definidos antes do layout (ver `wireframe-textual.md`).
- [x] A pagina responde as objecoes mapeadas no briefing (FAQ cobre 5 das 5).

## Copy e design

- [x] Primeiro viewport explica oferta (ortopedista em Brasilia para dor articular), publico (dor no joelho/ombro/quadril/coluna) e proxima acao (agendar via WhatsApp).
- [x] Provas sao reais (HBDF, Ceilandia EC, SBCJ, formacoes) e precedem os CTAs mais fortes.
- [x] Mapa visual preenchido com IDs de referencia e overrides justificados (ver `visual-map.md`).
- [x] Mobile revisado a 375px — CRM/RQE visiveis no primeiro viewport, CTAs em largura total, sem texto estourando.
- [x] Contraste do texto branco sobre `--dark #17323a` verificado (WCAG AA).

## Desenvolvimento

- [x] `<html lang="pt-BR">`, `meta viewport`, `title` e `meta description` presentes.
- [x] FAQ usa `<details>` nativo (sem JS pesado).
- [x] Fontes com `preconnect` e `display=swap`.
- [ ] **Eventos de conversao** — nao aplicavel no preview (sem GTM). Bloqueante para producao.
- [ ] **Performance com Lighthouse** — nao executado no preview. Bloqueante para producao.

## Spec saude.md

- [x] Identificacao profissional com CRM/RQE/TEOT visivel no primeiro viewport.
- [x] Nenhum trecho da copy contem promessa absoluta ("resolvo", "definitivo", "cura"), superlativo ("melhor", "unico") ou termo promocional.
- [x] Sem antes/depois, sem foto de paciente, sem depoimento com resultado quantificado.
- [x] Cirurgia do Joelho apresentada como **area de atuacao** (SBCJ 2023), nao como especialidade RQE.
- [x] Intervencionismo da Dor e Medicina Esportiva apresentados como **pos-graduacao**, nao como especialidade.
- [x] Sem numeros ou claims tecnicos sem fonte.
- [ ] **Politica de privacidade** linkada no rodape aponta para `#politica` (placeholder). Precisa apontar para URL real na producao.
- [ ] **Icones de card** — v1 sem icones por card (decisao registrada no `visual-map.md`). v2 precisa passar por contact sheet (`docs/repertorio-icones.md`).

## Spec google-ads.md

- [x] Titulo do hero coerente com o publico do anuncio (dor articular ortopedica em Brasilia).
- [x] CTA primario unico e visivel no primeiro viewport.
- [x] **Rodape sem telefone, WhatsApp direto ou canal fora do CTA rastreado.** Nenhum numero exposto em toda a pagina.
- [x] Todos os CTAs de WhatsApp apontam para `#agendar-bridge` (placeholder). Producao: bridge page real com `whatsapp_click` disparado antes do `wa.me`.
- [ ] **Consent Mode v2 + GTM** — nao presente no preview. Bloqueante para producao (ver `specs/google-ads.md`).
- [x] Preview esta com `noindex, follow` — apropriado para preview no GitHub Pages, deve ser removido em producao.

## Pendencias registradas em briefing.md (nao bloqueiam merge do preview, bloqueiam publicacao em Ads)

1. Endereco completo de JK Ortopedia e Neuri (CEP, sala, complemento).
2. Terceira unidade de atendimento (nome, endereco, horario).
3. Convenios aceitos por unidade.
4. Foto profissional do medico em consultorio (plano medio, olhando para camera).
5. URL da bridge page de conversao do Pulso.
6. Texto do anuncio Google Ads para confirmar message match do hero.
7. Politica de privacidade real (aproveitar template do `politica-de-privacidade.html` gerado para o Dr. Gustavo).
8. GTM ID + configuracao de Consent Mode v2.

## Regra de saida

Preview aprovado para validacao visual com o cliente. **Nao aprovado para publicacao em Ads** — precisa ao menos: URL de bridge, foto real, politica de privacidade real, GTM + Consent Mode v2, remocao do `noindex`, e resolucao dos pontos 1-3 (enderecos/convenios/terceira unidade).
