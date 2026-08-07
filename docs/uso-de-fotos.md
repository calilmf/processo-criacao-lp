# Uso de Fotos

Escolher foto de LP também é decisão visual, e tem falhas recorrentes que passam despercebidas em revisão só-de-texto. Este documento existe porque, numa LP de ortopedia real, a mesma foto do médico foi usada no hero **e** na seção autoridade — o resultado cansa e enfraquece o hero, e a revisão só pegou depois de publicado.

## Regra: não repetir a mesma foto

Nenhuma foto aparece duas vezes na mesma LP. Vale para o retrato do médico, para foto de consultório, para foto de procedimento — **nenhuma repete**. A regra é sobre foto **igual**, não sobre foto do médico.

Ter duas fotos diferentes do médico na página (uma no hero, outra na seção autoridade) é permitido e comum: hero costuma pedir foto mais formal/institucional; autoridade pode usar um retrato mais próximo/humano, ou foto do médico em contexto (atendendo, examinando, no consultório). O que importa é que sejam ensaios/registros distintos, não a mesma foto reaproveitada.

## Opções válidas para a foto da autoridade

Em ordem de preferência, quando a autoridade prevê uma coluna de foto:

1. **Outra foto do médico**, de um ensaio diferente do hero — retrato próximo/humano, ou foto em contexto (consultório, atendimento, procedimento respeitando as restrições de setor).
2. **Foto real do consultório ou ambiente de atendimento** — prova de que ele opera onde diz.
3. **Foto real de procedimento ou atendimento** — respeitando restrições de setor (sem paciente identificável, sem antes/depois, sem depoimento com resultado quantificado).
4. **Remover a coluna de foto** — usar autoridade só-texto (lista de credenciais em card único).

**Nunca** usar stock/render como fallback. Foto de banco quebra a spec de saúde e é visível a olho nu — o cérebro do visitante identifica "isso não é aqui" em milissegundos.

## Por que não repetir a mesma foto

- **Fadiga visual:** o mesmo rosto exato no mesmo enquadramento duas vezes na mesma página faz o leitor pular a segunda ocorrência.
- **Enfraquece o hero:** o retrato do hero é a âncora de identificação profissional (gate 1 da `specs/saude.md`). Quando reaparece idêntico, perde peso.
- **Sinaliza escassez de ativos:** repetir a mesma foto comunica "só tinha essa" — o oposto da mensagem de solidez que a seção autoridade precisa passar.

Duas fotos **diferentes** do médico não têm nenhum desses problemas — pelo contrário, sinalizam abundância de material e permitem alternar o tom (formal no hero, próximo na autoridade).

## Como aplicar

Na fase de **wireframe textual** (etapa 2 do `docs/processo-de-criacao.md`), quando a autoridade for prevista com foto, listar qual ativo será usado ali — e verificar que é distinto do ativo do hero. Se o único ativo disponível é a mesma foto do hero, redesenhar a seção autoridade sem foto na mesma etapa (opção 4 acima), ou pedir um segundo ensaio antes do build. Não adiar a decisão.

Registrar a decisão no `visual-map.md` do projeto na linha "Autoridade", explicitando qual foto vai onde.

## Restrições que já valem por outra spec

- Sem paciente identificável, sem antes/depois, sem depoimento com resultado quantificado — `specs/saude.md`.
- Sem stock/render — `specs/saude.md`.
- Sem foto meramente decorativa — `docs/repertorio-visual.md` §"O que nao colocar no repertorio".

Este documento cobre apenas a regra visual de **não repetir a mesma foto**. As demais restrições continuam nos seus lugares.
