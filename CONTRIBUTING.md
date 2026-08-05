# Como Contribuir

Este repositorio prioriza clareza de decisao. Antes de adicionar qualquer material, escolha a camada correta:

- Uma regra obrigatoria vai para uma spec.
- Um novo passo ou gate vai para o processo.
- Um item verificavel vai para um checklist.
- Um formulario reutilizavel vai para um template.
- Uma referencia estetica vai para o repertorio somente depois de analisada.

## Para adicionar uma referencia visual

Nao adicione apenas um link. Crie um cartao com ID estavel e registre:

1. O que a referencia ensina.
2. Em quais secoes ou contextos ela funciona.
3. O que pode ser reinterpretado sem copiar.
4. Riscos de uso: performance, acessibilidade, compliance ou excesso visual.
5. Referencias que combinam com ela.

## Para melhorar um checklist

Adicione um item quando ele evitar um problema que realmente apareceu em uma entrega. Itens devem ser objetivos o bastante para receber `sim`, `nao` ou uma pendencia identificada.

## Para estender a biblioteca de icones por especialidade

Ao validar um novo icone como bucket A (match literal) para uma especialidade, adicione a linha em `especialidades/<especialidade>/icones-base.md` (crie o arquivo se a especialidade ainda nao tiver um). Ao identificar um novo token de dominio clinico que um verificador automatico de icones deveria barrar fora do dominio certo (ex: termos de outra especialidade), estenda a lista de tokens no script de verificacao do repo de LP correspondente e documente o motivo — nao adicione um token sem um caso real que o justifique.
