# Spec: LP de Google Ads

Contrato minimo para Landing Pages destinadas a campanhas pagas (Google Ads, Meta Ads, Kwai Ads). O objetivo e proteger o Quality Score, a atribuicao de conversao e a coerencia entre anuncio e pagina.

## Message match

- Titulo do hero repete a promessa central do anuncio (verbo + beneficio + publico).
- Se a campanha tem varios anuncios, cada grupo aponta para uma LP ou secao com match especifico. Nao mandar todo o trafego para uma pagina generica.
- A imagem ou cor dominante do hero conversa com o criativo do anuncio quando possivel.

## CTA e conversao

- Um unico CTA primario por LP. CTAs secundarios podem existir, mas nao podem competir por atencao no primeiro viewport.
- **Rodape sem telefone, WhatsApp direto, e-mail ou qualquer canal fora do CTA rastreado.** Toda conversao precisa passar por evento mensuravel. Um canal solto no rodape vaza conversao e destroi a atribuicao da campanha.
- Formulario curto: nome, telefone e no maximo um campo condicional. Cada campo extra reduz CVR.
- Politica de privacidade linkada. Consentimento LGPD explicito antes do submit.

## Tracking

- GA4 ou GTM configurado antes do deploy, nao depois.
- Evento de conversao (form_submit, whatsapp_click, phone_click quando aplicavel) testado com o proprio DevTools antes de ligar a campanha.
- Se o CTA leva a WhatsApp, usar link com evento antes do `wa.me`.
- Google Tag ou Meta Pixel disparando pageview e evento de conversao. Verificar em Tag Assistant ou equivalente.

## Performance e mobile

- LCP < 2,5s em conexao mobile 4G. Imagens em WebP, fontes com `preconnect` e `display=swap`.
- Hero e CTA renderizados sem depender de scroll no viewport 375px.
- Nenhuma imagem decorativa carrega antes de promessa e CTA aparecerem.
- Formulario funciona com teclado virtual sem esconder o botao de submit.

## Indexacao

- **Nao** usar `noindex` em producao — historial de LP afeta Quality Score futuro.
- Meta description coerente com o anuncio.
- URL curta, legivel e sem parametros de tracking indexaveis.

## Coerencia com o setor

- Se a LP e de saude, tambem se aplica `specs/saude.md`. Regras se somam, nao se substituem.
- Se a oferta e produto, tambem se aplica `specs/ecommerce.md`.

## Gates

- [ ] Titulo do hero faz message match com o anuncio.
- [ ] CTA primario e unico e visivel no primeiro viewport.
- [ ] Rodape nao contem telefone, WhatsApp ou canal direto sem tracking.
- [ ] Evento de conversao configurado e testado.
- [ ] LCP mobile abaixo de 2,5s.
- [ ] Politica de privacidade linkada e consentimento LGPD antes do submit.
- [ ] Pagina indexavel (nenhum `noindex` acidental).
