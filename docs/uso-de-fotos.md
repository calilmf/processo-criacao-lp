# Uso de Fotos

Escolher foto de LP também é decisão visual, e tem falhas recorrentes que passam despercebidas em revisão só-de-texto. Este documento existe porque, numa LP de ortopedia real, a mesma foto do médico foi usada no hero **e** na seção autoridade — o resultado cansa e enfraquece o hero, e a revisão só pegou depois de publicado.

## Regra: retrato do médico aparece uma vez só

Em LP de médico, o retrato do profissional entra **uma única vez** na página — normalmente no hero. A seção de autoridade **não** repete a mesma foto, nem outra foto do médico do mesmo ensaio.

Opções válidas para a foto da autoridade, em ordem de preferência:

1. **Foto real do consultório ou ambiente de atendimento** — prova de que ele opera onde diz.
2. **Foto real de procedimento ou atendimento** — respeitando as restrições de setor (sem paciente identificável, sem antes/depois, sem depoimento com resultado quantificado).
3. **Remover a coluna de foto** — usar autoridade só-texto (lista de credenciais em card único).

**Nunca** usar stock/render como fallback. Foto de banco quebra a spec de saúde e é visível a olho nu — o cérebro do visitante identifica "isso não é aqui" em milissegundos.

## Por que não repetir o retrato

- **Fadiga visual:** o mesmo rosto duas vezes na mesma página faz o leitor pular a segunda ocorrência.
- **Enfraquece o hero:** o retrato do hero é a âncora de identificação profissional (gate 1 da `specs/saude.md`). Quando reaparece, perde peso — a autoridade textual da segunda seção passa a competir com uma imagem que já foi vista.
- **Sinaliza escassez de ativos:** repetir foto comunica "só tinha essa" — o oposto da mensagem de solidez que a seção autoridade precisa passar.

## Como aplicar

Na fase de **wireframe textual** (etapa 2 do `docs/processo-de-criacao.md`), quando a autoridade for prevista com foto, listar qual ativo será usado ali — e verificar que é distinto do ativo do hero. Se o único ativo disponível é o retrato do médico, redesenhar a seção autoridade sem foto na mesma etapa. Não adiar a decisão para o build.

Registrar a decisão no `visual-map.md` do projeto na linha "Autoridade", explicitando qual foto vai onde.

## Restrições que já valem por outra spec

- Sem paciente identificável, sem antes/depois, sem depoimento com resultado quantificado — `specs/saude.md`.
- Sem stock/render — `specs/saude.md`.
- Sem foto meramente decorativa — `docs/repertorio-visual.md` §"O que nao colocar no repertorio".

Este documento cobre apenas a regra visual de **não repetir o retrato do médico**. As demais restrições continuam nos seus lugares.
