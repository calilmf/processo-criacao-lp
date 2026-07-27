# Repertorio de Icones

Icone de card e uma decisao de precisao clinica, nao apenas uma decisao estetica. O modo de falha aqui e diferente do repertorio visual: um icone errado nao deixa a pagina "feia", ele comunica o dominio clinico errado (ex: um icone de pulso cardiaco numa pagina de ortopedia) ou nenhum dominio (ex: um cadeado generico de seguranca num card de sintoma medico). Por isso a escolha de icones tem um processo proprio, separado do repertorio visual geral.

## A regra dura

Um icone so pode ser escolhido pelo que seu nome/dominio realmente significa, nunca pela forma que evoca. "Parece um alerta", "parece travado", "parece uma onda" nao sao motivo valido de escolha quando essa forma vem de um icone de dominio clinico diferente do card, ou de um icone sem nenhum dominio clinico (cadeado, engrenagem, seta).

Teste pratico: leia o nome oficial do icone em voz alta, sem olhar a imagem. Se o nome nao descreve o conceito do card, o icone esta errado — nao importa o quanto a forma pareca combinar.

## Metodo de selecao, por card

Para cada card `(titulo, descricao)`, antes de tocar em qualquer buscador de icones:

### 1. Extrair o conceito clinico literal

Escreva uma frase curta do que o card realmente significa clinicamente, e o dominio dele. Exemplo: "Crises recorrentes" numa pagina de coluna nao e "um alerta generico" — e "piora recorrente de dor na coluna", dominio = coluna/ortopedia.

### 2. Buscar nesta ordem fixa, sem pular etapa

1. **`healthicons`** primeiro, sempre. E o unico set do Iconify feito para conceitos clinicos e de saude global de forma literal (spine, back-pain, joints, nerve, foot, orthopaedics, orthotics, sling, cast, cane, crutches, traumatism, walk-supported, skeleton, pain, stethoscope, syringe, xray, weights, walking, physical-therapy, occupational-therapy).
2. **`material-symbols`** segundo, apenas para substantivos anatomicos especificos que faltam no healthicons (ossos e articulacoes por nome: femur, wrist, ulna-radius, foot-bones, hand-bones, front-hand). Nunca usar este set para conceitos abstratos/emocionais (alerta, urgencia, humor) so porque ele tambem tem esses icones — foi exatamente assim que um icone de pulso cardiaco (`pulse-alert-outline`) foi escolhido por engano para um card de coluna.
3. **`hugeicons`** terceiro, so como ultimo recurso de forma literal (hoje usado apenas para `shoulder`).
4. Qualquer outro set do Iconify: so com busca explicita, documentada no mapa de icones (nunca escolha silenciosa).

### 3. Classificar em um dos 3 buckets

Somente o bucket A pode ser usado sem sinalizacao no mapa de icones. B e C sempre precisam de justificativa escrita.

- **Bucket A — Match literal.** O nome oficial do icone descreve exatamente o conceito do card, no mesmo dominio clinico. Passa no teste da regra dura.
- **Bucket B — Composto literal.** Nenhum icone sozinho serve, mas dois icones literais do mesmo dominio, combinados, comunicam o conceito (ex: `healthicons:spine-outline` + um simbolo de alerta, para "crise recorrente de coluna" — os dois elementos sao literais e do mesmo dominio, nenhum e emprestado de um dominio errado). Como a maioria dos sites de LP renderiza um unico `<img>` por card, um icone composto vira **um SVG customizado unico**, desenhado combinando os dois elementos graficos — nao duas tags de imagem sobrepostas via CSS. Este e o padrao preferido quando nao existe icone literal (ver regra abaixo).
- **Bucket C — Fallback generico documentado.** So depois de confirmar, por busca real, que nao existe icone literal nem combinacao possivel (ex: termos como "meniscus", "ganglion cyst", "trigger finger", "bursitis", "ligament", "crepitus", "carpal tunnel", "frozen shoulder", "ankle sprain" nao existem em nenhum set do Iconify hoje). Mesmo assim, o fallback tem que ficar no mesmo dominio/regiao do card — nunca emprestar de uma especialidade errada — e ser escrito no mapa de icones com a razao. Bucket C deve ser raro: na duvida, prefira compor (bucket B) a aceitar um fallback solto.

### 4. Checar contra os icones ja usados na mesma pagina

Nao repetir o mesmo icone em cards diferentes da mesma pagina — nem dentro da mesma secao (sintomas/causas/cuidados), nem entre secoes diferentes da mesma pagina. Um verificador automatico deve rodar isso antes do build (ver `docs/checklists.md`).

## Quando nao existe icone literal em lugar nenhum

Confirmado por busca real no Iconify (nao suposicao): conceitos ortopedicos especificos como menisco, cisto, dedo em gatilho, bursite, ligamento, crepitacao, tunel do carpo, ombro congelado e entorse de tornozelo nao tem icone literal proprio em nenhum set indexado. Nestes casos o padrao e **compor dois icones literais do mesmo dominio** (bucket B) — por exemplo, o icone da regiao do corpo (joelho/ombro/coluna) combinado com um simbolo generico mas clinicamente neutro (alerta, gesso, orteses) — em vez de aceitar um icone de forma parecida vindo de outro dominio.

## Biblioteca por especialidade

Cada especialidade medica atendida pelas LPs deve ter uma lista curada de icones ja validados como bucket A, para quem for construir a proxima LP daquela especialidade nao precisar redescobrir do zero. Ver `especialidades/ortopedia/icones-base.md` como primeiro exemplo. Quando uma nova especialidade aparecer, criar `especialidades/<especialidade>/icones-base.md` do mesmo jeito — nunca forcar a lista de uma especialidade a absorver icones de outro dominio.

## Onde isso se conecta no processo

A escolha de icones acontece na fase de Copy (ver `docs/processo-de-criacao.md`), documentada no template `templates/mapa-icones.md`, antes do build. O gate correspondente esta em `docs/checklists.md`.
