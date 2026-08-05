# ref.visual.forward.saude-humana-clara

**Tom:** humano, clinico, acolhedor sem infantilizar
**Fonte:** Forward (clinica de atencao primaria nos EUA) e clinicas premium brasileiras equivalentes

## O que ensina

LP de saude que sai do padrao "azul institucional + medico de bracos cruzados". Fundo claro com paleta terrosa ou verde-agua, tipografia serifada em titulo, sans em corpo, foto real do profissional em ambiente natural (nao estudio branco). Autoridade vem da identificacao formal (CRM, RQE, formacao) exibida com peso — nao escondida em um roda-pe.

## Secoes onde funciona

- Hero de LP medica.
- Autoridade / apresentacao do profissional.
- Provas detalhadas (depoimentos com identificacao).

## Elementos para reinterpretar

- Paleta terrosa: `--paper` como base, `--sand` como acento quente, `--teal` ou `--green` como cor de confianca.
- Foto do profissional em plano medio, olhando para camera, ambiente do consultorio ao fundo desfocado.
- CRM/RQE em subtitulo do nome do medico — mesma fonte, peso menor, cor `--muted`.
- Depoimentos com nome completo do paciente (com consentimento), sem estrelas de review comercial.
- Espaco negativo entre secoes maior do que o usual em SaaS — o ritmo e mais calmo.

## Riscos de copiar

- Foto de banco de imagens quebra o tom. Precisa ser foto real ou nao usar foto.
- Depoimento com resultado quantificado ("emagreci 12kg") viola `specs/saude.md`.
- Antes/depois de procedimento viola CFM. Nao usar mesmo que a referencia use.
- Serifada em corpo de texto reduz legibilidade — usar so em titulo.

## Combinacoes sugeridas

- `ref.visual.stripe.narrativa-clara-espacosa` para secoes de mecanismo e diferenciais.
- `ref.visual.notion.faq-progressivo-limpo` para FAQ de objecoes.
- `ref.visual.cal.formulario-embutido-simples` para o CTA final em LP organica; em Ads, seguir `specs/google-ads.md`.

## Restricoes

- **Performance:** fotos reais em WebP com `loading="lazy"` fora do first viewport.
- **Acessibilidade:** cores terrosas em texto corpo precisam contraste 4.5:1 verificado.
- **Setor:** `specs/saude.md` sempre. Se for LP de Ads, tambem `specs/google-ads.md`.
