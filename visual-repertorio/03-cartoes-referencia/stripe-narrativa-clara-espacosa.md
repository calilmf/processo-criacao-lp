# ref.visual.stripe.narrativa-clara-espacosa

**Tom:** institucional, confiavel, editorial em fundo claro
**Fonte:** Stripe (infraestrutura de pagamentos)

## O que ensina

Secoes com muito respiro vertical, tipografia com peso variado (regular + bold no mesmo bloco) e uma decisao visual por secao — nao tres. Cada scroll revela uma unica ideia. Cor usada com disciplina: acento pontual em CTAs e destaques, resto em preto/cinza/branco.

## Secoes onde funciona

- Solucao / mecanismo.
- Diferenciais e beneficios.
- Autoridade institucional.

## Elementos para reinterpretar

- Padding vertical amplo entre secoes (80-120px desktop).
- Titulo de secao em 40-48px, subtitulo em 18-20px com cor `--muted`.
- Duas colunas com peso desigual (1.1fr / 0.7fr) — titulo do lado grande, apoio do lado pequeno.
- Cards em fundo branco com borda leve (`--line`), radius 8, padding 26.
- Iconografia linear, um unico peso, cor `--teal`.

## Riscos de copiar

- Fundo claro com pouca cor exige copy forte. Se o texto for generico, a secao parece vazia.
- Duas colunas viram uma so em mobile — planejar a queda antes do build.
- Grid de cards com 4 colunas fica ilegivel em tablet sem breakpoint intermediario.
- Muito respiro em LP de Ads pode empurrar o CTA para baixo do LCP — vigiar.

## Combinacoes sugeridas

- `ref.visual.linear.hero-editorial-serifado` para o hero, seguido de Stripe nas secoes internas.
- `ref.visual.notion.faq-progressivo-limpo` no fim, mesma familia estetica.

## Restricoes

- **Performance:** cards com sombras suaves custam menos que gradientes; preferir sombra.
- **Acessibilidade:** cinza `--muted` em fundo claro precisa passar 4.5:1 em texto corpo.
- **Setor:** neutro. Aplica em qualquer spec.
