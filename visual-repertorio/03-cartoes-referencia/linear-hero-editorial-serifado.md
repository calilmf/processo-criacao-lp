# ref.visual.linear.hero-editorial-serifado

**Tom:** editorial, restrained, tech premium
**Fonte:** Linear (ferramenta de gestao de produto)

## O que ensina

Hero em fundo escuro com tipografia oversized e hierarquia jornalistica. Toda a autoridade vem do peso e do tamanho do texto — nao de bordas, cores fortes ou ilustracoes. O CTA e pequeno em area mas alto em contraste. Espaco negativo generoso separa o titulo de tudo o mais.

## Secoes onde funciona

- Hero de LP de servico profissional (juridico, consultoria, medico premium).
- Autoridade e apresentacao do profissional ou empresa.

## Elementos para reinterpretar

- Titulo oversized com `clamp(40px, 6vw, 68px)` ou maior.
- Fundo escuro com um unico acento de cor. Nunca dois.
- Espacamento vertical amplo acima e abaixo do titulo.
- CTA de dimensao modesta, alto peso tipografico, cor de acento.
- Kicker curto acima do titulo, uppercase e tracking positivo.

## Riscos de copiar

- Tipografia oversized quebra em mobile sem `clamp()` bem calibrado.
- Fundo escuro exige revisao de contraste WCAG AA (4.5:1 minimo).
- "Restrained" mal executado vira "vazio". Se a copy nao carrega, o hero perde sentido.
- Em saude, esconder CRM/RQE atras do minimalismo viola `specs/saude.md`.

## Combinacoes sugeridas

- `ref.visual.stripe.narrativa-clara-espacosa` para secoes seguintes em fundo claro — mantem o restrained.
- `ref.visual.forward.saude-humana-clara` quando o setor pede calor no lugar de sobriedade tech.

## Restricoes

- **Performance:** fonte custom exige `preconnect` e `font-display: swap`.
- **Acessibilidade:** contraste medido, foco visivel em cor de acento.
- **Setor:** saude deve preservar identificacao profissional no hero, mesmo com estetica minimal.
