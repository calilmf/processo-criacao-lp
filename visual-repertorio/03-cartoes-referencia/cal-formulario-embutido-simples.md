# ref.visual.cal.formulario-embutido-simples

**Tom:** utilitario, baixa friccao, decisao imediata
**Fonte:** Cal.com e agendadores minimalistas equivalentes

## O que ensina

Formulario ou agendador embutido no CTA final em vez de botao que abre modal ou navega para outra pagina. O visitante nao precisa clicar duas vezes — a acao esta na frente dele. Design do formulario e proprio da LP (mesma paleta, mesmo radius, mesma tipografia), nao um embed generico que quebra a estetica.

## Secoes onde funciona

- CTA final de LP de servico com agendamento.
- Hero de LP transacional (ex: calculadora, cotacao rapida).
- CTA intermediario em LP longa quando a conversao pode acontecer antes do fim.

## Elementos para reinterpretar

- Formulario de 2-3 campos maximo. Nome, telefone, data ou horario preferido.
- Botao de submit ocupando 100% da largura do formulario em mobile.
- Feedback de estado inline (erro, sucesso) sem redirecionar.
- Placeholder curto e label persistente acima do campo — nao substituir label por placeholder.
- Consentimento LGPD como checkbox pequeno abaixo do submit, nao modal.

## Riscos de copiar

- Formulario embutido em LP de Ads sem tracking de `form_submit` perde a conversao.
- Campos demais aumentam friccao. Cada campo extra abaixa CVR.
- Embed de terceiro sem estilizacao quebra o tom da pagina.
- Se o agendador depende de JS pesado, o LCP sobe — vigiar.

## Combinacoes sugeridas

- `ref.visual.forward.saude-humana-clara` para LP de saude com agendamento direto.
- `ref.visual.stripe.narrativa-clara-espacosa` nas secoes anteriores para preparar a decisao.

## Restricoes

- **Performance:** se e embed de terceiro, carregar so no viewport (`IntersectionObserver` ou `loading="lazy"` para iframe).
- **Acessibilidade:** labels persistentes, ordem de tab correta, mensagens de erro associadas ao campo por `aria-describedby`.
- **Setor:** em Ads, sempre com `specs/google-ads.md` (evento de conversao testado). Em saude, campos minimos + consentimento LGPD antes do submit.
