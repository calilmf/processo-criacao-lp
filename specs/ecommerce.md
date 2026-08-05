# Spec: LP de E-commerce

Contrato minimo para Landing Pages de produto, colecao ou oferta com checkout. O objetivo e reduzir a friccao de decisao e cumprir as obrigacoes do Codigo de Defesa do Consumidor (CDC).

## Prova de produto

- Fotos reais em multiplos angulos. Frente, verso, detalhe e escala (mao, ambiente ou objeto de referencia).
- Video curto de uso quando o produto tem funcionamento nao obvio.
- Especificacoes tecnicas: dimensoes, peso, materiais, cores disponiveis, voltagem, garantia.
- Nao apresentar render ou mockup como foto de produto real.

## Preco e pagamento

- Preco a vista claro. Se ha parcelamento, taxa efetiva visivel — sem "de/por" simulado.
- Formas de pagamento aceitas exibidas antes do checkout, nao dentro dele. Surpreender no ultimo passo aumenta abandono.
- Se ha frete gratis, condicao clara (valor minimo, regiao, prazo).

## Frete e entrega

- Calculadora de frete por CEP acessivel antes do checkout — prazo + valor.
- Se a entrega depende de regiao, informar cobertura antes do usuario tentar comprar.
- Nao esconder custos de envio ate a ultima etapa.

## Estoque

- Estado de estoque real: "em estoque", "ultimas unidades" (somente se verdadeiro), "sob consulta" ou "esgotado".
- Nao usar contador falso de urgencia ou "restam N pessoas vendo agora" sem fonte real.

## Politica de devolucao

- Politica de arrependimento visivel — o CDC (art. 49) garante 7 dias corridos para compras a distancia. Nao restringir esse direito.
- Prazo total de troca ou devolucao claro, com forma de solicitacao (email, formulario, canal proprio).
- Politica linkada no footer e proxima ao CTA de compra.

## Reviews e prova social

- Reviews reais, nao editados. Se o cliente pode avaliar, exibir a distribuicao (5/4/3/2/1 estrelas), nao apenas a media.
- Data da review visivel. Sem selo generico "produto mais vendido" sem criterio publicado.
- Foto de cliente com consentimento registrado.

## Checkout

- Guest checkout disponivel quando possivel. Forcar cadastro derruba conversao.
- Numero de passos visivel (1 de 3, 2 de 3, etc.).
- Politica de privacidade linkada. Consentimento LGPD explicito antes de finalizar.

## Seguranca

- SSL ativo (a plataforma cuida, mas verificar).
- Selo do gateway de pagamento (Pagar.me, Mercado Pago, Cielo, Stripe etc.) com nome real, nao icone generico.
- Nao usar selos ficticios de seguranca sem link de verificacao.

## Suporte

- Canal de suporte visivel (chat, email, formulario, WhatsApp).
- Diferente de Ads: em e-commerce, canal direto ajuda a converter e nao vaza atribuicao — o pixel de compra dispara no checkout, nao no clique de contato.

## Gates

- [ ] Fotos de produto reais em mais de um angulo, com escala.
- [ ] Especificacoes tecnicas completas visiveis sem clique adicional.
- [ ] Preco a vista e taxa de parcelamento claros.
- [ ] Frete calculavel por CEP antes do checkout.
- [ ] Politica de devolucao visivel e compativel com CDC art. 49.
- [ ] Reviews mostram distribuicao, nao so media.
- [ ] Guest checkout disponivel ou justificativa registrada.
- [ ] Selo de gateway real, sem selos ficticios.
