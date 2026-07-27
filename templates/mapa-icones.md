# Mapa de Icones

Preencha por pagina/regiao, na fase de Copy, antes do mapa visual e do build. Uma linha por card (sintomas, causas e cuidados). Siga o metodo completo em `docs/repertorio-icones.md`.

| Secao | Card (titulo) | Conceito literal | Dominio clinico | Icone escolhido | Bucket (A/B/C) | Justificativa | Fonte (set:nome) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sintomas | Dor lombar persistente | Dor na parte baixa das costas | Coluna/ortopedia | healthicons:back-pain-outline | A | Nome do icone descreve exatamente o conceito | healthicons |
| Sintomas | Crises recorrentes | Crise/piora recorrente de dor na coluna | Coluna/ortopedia | SVG customizado: coluna + alerta | B | Sem icone literal para "crise recorrente"; composto por dois elementos literais do mesmo dominio (coluna + alerta), nenhum emprestado de dominio errado | healthicons (spine) + material-symbols (dangerous), combinados num SVG unico |

## Regra de bloqueio

- Nenhuma linha pode ser bucket C sem justificativa escrita confirmando que a busca por icone literal e por composicao (bucket B) foi feita e falhou.
- Nenhum icone pode ser aprovado so pela forma ("parece um alerta", "parece travado") sem que o nome/dominio do icone seja coerente com o card.
- Antes do build, rode o verificador automatico de icones (duplicidade na pagina inteira + checagem de dominio) e resolva todos os apontamentos.
