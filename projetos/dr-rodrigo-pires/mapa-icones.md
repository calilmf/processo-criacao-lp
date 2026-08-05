# Mapa de Ícones — Dr. Rodrigo Pires

Preenchido na fase de Copy, antes do build. Método completo em `docs/repertorio-icones.md`.

## Processo executado

1. **Cards.json** com 6 cards + 5 termos de busca cada.
2. **`ferramentas/harvest-candidatos.py`** rodado em toda a Iconify (215 sets, 340 candidatos brutos, 67 baixados após filtro).
3. **`ferramentas/contact-sheet.py`** gerou HTML com cada candidato a 32px e 96px lado a lado.
4. **Revisão visual** feita no browser — olhando a 32px, sem ler o nome, decidir se comunica o serviço do card.

## Escolha por card

| Seção | Card | O que o desenho mostra | Arquivo | Ícone de origem | Conferido a 32px | Bucket |
| --- | --- | --- | --- | --- | --- | --- |
| Serviços | Consulta ortopédica | Estetoscópio médico em contorno | `rodrigo-pires/consulta-ortopedica.svg` | `material-symbols:stethoscope-outline` | sim | A |
| Serviços | Ultrassonografia musculoesquelética | Transducer de ultrassom com ondas saindo | `rodrigo-pires/ultrassonografia.svg` | `healthicons:ultrasound-scanner-outline` | sim | A |
| Serviços | Infiltrações e bloqueios | Seringa clínica clara | `rodrigo-pires/infiltracoes-e-bloqueios.svg` | `healthicons:syringe-outline` | sim | A |
| Serviços | Medicina regenerativa (PRP) | Três células/glóbulos sanguíneos agrupados | `rodrigo-pires/medicina-regenerativa.svg` | `healthicons:blood-cells-outline` | sim | A |
| Serviços | Cirurgia do joelho | Anatomia articular clara de joelho | `rodrigo-pires/cirurgia-do-joelho.svg` | `game-icons:knee-cap` | sim | A |
| Serviços | Medicina esportiva | Pessoa correndo | `rodrigo-pires/medicina-esportiva.svg` | `healthicons:running-outline` | sim | A |

Todos bucket A (match literal), zero bucket B (composto) ou C (fallback).

## Card removido durante o processo

**Terapia por onda de choque** — considerado inicialmente como card com ícone próprio, mas confirmado por harvest que nenhum ícone literal existe em toda a Iconify. As alternativas eram:

- `game-icons:big-wave` — parece surf, não médico.
- `material-symbols:vibration-outline` — barras verticais que não comunicam "onda de choque".
- Vários `game-icons:*-impact` — bullet, meteor, anvil, screen — todos de outro domínio.

Decisão: em vez de forçar bucket C com ícone ambíguo, **remover o card** e consolidar "onda de choque" dentro do card de "Infiltrações e bloqueios" no texto. Card removido tem menos custo que ícone ambíguo. Isso é seguir `docs/repertorio-icones.md` §"Sem ícone literal em lugar nenhum".

## Regra de pasta

Todos os arquivos vivem em `assets/topic-icons/rodrigo-pires/`. A LP `previews/dr-rodrigo-pires.html` **só usa ícones dessa pasta**. Regra estrutural — ícone de outra especialidade fica geograficamente impossível.

## Ícones já validados aproveitados de `especialidades/ortopedia/conceitos.md`

- `healthicons:stethoscope-outline` — usado no Dr. Thiago Cerqueira. Escolhi variante `material-symbols` porque a `healthicons` renderiza com traço menos contrastado a 32px no fundo claro — a diferença ficou clara no contact sheet.
- `healthicons:ultrasound-scanner-outline` — mesmo ícone validado.
- `healthicons:syringe-outline` — mesmo ícone validado.
- `game-icons:knee-cap` — mesmo ícone validado.
- `healthicons:running-outline` — mesmo conceito (a variante `outline` foi baixada diretamente da Iconify API).

**Ícone novo** (não estava em conceitos.md):
- `healthicons:blood-cells-outline` — validado agora para "medicina regenerativa (PRP)". Vale registrar em `conceitos.md` numa próxima PR de manutenção do repo.
