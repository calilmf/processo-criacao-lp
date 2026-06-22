# Arquitetura da Brain

Uma brain de Landing Pages funciona melhor quando conhecimento, obrigacao e verificacao nao moram no mesmo documento. Cada camada tem uma responsabilidade distinta.

| Pasta ou camada | Funcao | Nao deve virar |
| --- | --- | --- |
| `knowledge/` | Explica como pensar: estrategia, copy, UX, desenvolvimento e referencias. | Regra obrigatoria escondida em texto longo. |
| `specs/` | Define o contrato minimo da LP. | Biblioteca de inspiracao ou lista de opinioes. |
| `skills/` | Organiza a execucao em fases e gates. | Um texto de dicas sem ordem. |
| `checklists/` | Audita o resultado item por item. | Uma revisao subjetiva de memoria. |
| `templates/` | Padroniza os artefatos que precisam ser preenchidos. | Documento final sem campos de decisao. |
| `visual-repertorio/` | Guarda referencias esteticas que podem ser recuperadas por contexto. | Colecao de URLs sem analise. |

## Por que essa separacao importa

Quando uma regra obrigatoria fica no meio de uma referencia estetica, ela deixa de ser percebida como obrigacao. Quando um checklist vira prosa, ele deixa de funcionar como gate. Quando uma referencia e apenas um link, ela nao ajuda a decidir o layout de uma secao.

A arquitetura cria um caminho de consulta:

1. A `spec` delimita o que a pagina precisa cumprir.
2. A `skill` diz quando consultar cada tipo de material.
3. O `template` registra as decisoes tomadas.
4. O `checklist` confirma que a decisao chegou ao resultado final.

## Gates

Um gate e uma condicao verificavel para seguir de fase. Exemplos:

- Nao escrever a copy antes de definir promessa, prova e CTA.
- Nao iniciar o layout sem um mapa visual por secao.
- Nao declarar entrega sem rodar o checklist final.

Gates nao servem para burocratizar. Eles protegem as etapas em que e facil assumir algo, esquecer uma restricao ou trocar uma decisao estrategica por um impulso visual.

## Adaptacao por contexto

O nucleo pode ser comum a quase toda LP, mas setores regulados, campanhas de midia paga e produtos complexos pedem extensoes. Elas devem viver como specs ou checklists complementares, sem deformar o fluxo base.

Exemplos de extensoes:

- Saude: regras de publicidade da profissao, identificacao profissional e revisao de claims.
- Google Ads: coerencia entre anuncio e hero, tracking, baixa friccao e politica de indexacao.
- E-commerce: prova de produto, estoque, frete, devolucao e checkout.
