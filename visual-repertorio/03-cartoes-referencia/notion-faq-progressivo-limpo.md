# ref.visual.notion.faq-progressivo-limpo

**Tom:** conversacional, disclosure natural, sem exagero grafico
**Fonte:** Notion, Linear docs e paginas de documentacao com FAQ integrado

## O que ensina

FAQ usando o elemento nativo `<details>`/`<summary>` — sem accordion custom em JS, sem icones piscando, sem animacao pesada. Pergunta e resposta parecem conteudo continuo, nao um widget separado. O visitante que ja tem confianca ignora; o que tem duvida abre.

## Secoes onde funciona

- FAQ de objecoes.
- Suporte / esclarecimento de politica (devolucao, garantia, cobertura).
- Bloco de duvidas antes do CTA final.

## Elementos para reinterpretar

- `<details>` nativo, sem JS. Borda superior fina separando itens.
- `<summary>` em peso 800, tamanho 18px, cursor pointer.
- Resposta em `--muted`, indentacao zero — nao encaixar mais fundo que a pergunta.
- Sem icones de "+/-" ou setas animadas. O browser ja indica estado.
- Uma unica pergunta aberta por vez nao e obrigatorio — deixar o visitante controlar.

## Riscos de copiar

- FAQ virando lista de perguntas que nao sao dele. Cada item precisa responder objecao real, nao SEO.
- Respostas longas demais ficam ilegiveis em mobile — cortar em 2-3 linhas quando possivel.
- Copiar accordion custom com animacao complexa desfaz o principal beneficio (peso zero).
- Em LP de saude, resposta com claim tecnico precisa fonte (`specs/saude.md`).

## Combinacoes sugeridas

- Praticamente qualquer hero — o padrao FAQ e neutro estetico.
- `ref.visual.forward.saude-humana-clara` para LP medica.
- `ref.visual.stripe.narrativa-clara-espacosa` para institucional.

## Restricoes

- **Performance:** zero. `<details>` e nativo, sem JS, sem CSS pesado.
- **Acessibilidade:** ja e acessivel por default (teclado, screen reader). Nao substituir por div+JS.
- **Setor:** em saude, revisar respostas contra `specs/saude.md`. Em ecommerce, FAQ de frete/devolucao tem que refletir a politica real (`specs/ecommerce.md`).
