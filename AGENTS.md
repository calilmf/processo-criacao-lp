# Instrucoes para Agentes

Este repo documenta o processo para criar Landing Pages. Se voce foi invocado para criar, revisar ou refatorar uma LP, siga esta ordem sem pular etapas. Gates existem para reduzir oscilacao de qualidade entre entregas.

## Antes de gerar qualquer HTML

1. Leia `docs/processo-de-criacao.md` inteiro.
2. Preencha `templates/briefing-lp.md` no arquivo do projeto. Campos sem dado confirmado recebem `[A VALIDAR]`. Nunca invente depoimento, numero, CRM, RQE, preco, prazo ou promessa.
3. Identifique o setor e a fonte de trafego. Se existir spec aplicavel em `specs/` (saude, google-ads, ecommerce, etc.), trate como contrato obrigatorio.
4. Preencha `templates/wireframe-textual.md` antes de escrever copy.
5. Escreva a copy por secao, usando a estrategia como limite.
6. Se a pagina usa icones por card (sintomas, causas, cuidados, procedimentos), preencha `templates/mapa-icones.md` seguindo `docs/repertorio-icones.md` — colher candidatos com `ferramentas/harvest-candidatos.py`, gerar contact sheet com `ferramentas/contact-sheet.py`, e escolher **olhando** a 32px. Nenhum icone e aprovado por nome.
7. Preencha `templates/visual-map.md` antes do layout. Use IDs concretos de `visual-repertorio/` quando existirem; se ainda nao existirem, registre a decisao visual em prosa curta.

## Ao construir a LP

- **Comece de `assets/tokens.css`.** Nao reinvente paleta, tipografia, escala tipografica ou radius do zero. Cada override do token base precisa de justificativa registrada no mapa visual.
- Toda LP em `previews/` precisa ter `<html lang="pt-BR">`, `meta viewport`, `title` descritivo e `meta description`.
- CTA primario preserva verbo, destino, prioridade e tracking definidos no briefing. Referencia visual pode influenciar contraste, espacamento e microinteracao — nao pode alterar a acao.
- Mobile e revisado no build, nao depois. Textos nao estouram, controles alcancam 44px de alvo.
- Imagens e icones tem funcao. Se nao explicam ou reforcam, saem.
- **Icone de card e decisao clinica, nao estetica.** Card da pagina `X` so pode usar arquivo de `assets/topic-icons/X/`. Icone de dominio errado (joelho em pagina de coluna, pulso cardiaco em ortopedia) e falha bloqueante — ver `docs/repertorio-icones.md`.

## Regras por tipo de pagina

- **Google Ads:** siga `specs/google-ads.md` quando existir. Regra base: rodape sem telefone ou canal direto que vaze conversao fora do CTA rastreado.
- **Saude:** siga `specs/saude.md` quando existir. Regra base: CRM/RQE visiveis, sem promessa de resultado, sem antes/depois em desacordo com a resolucao do CFM.
- **E-commerce:** siga `specs/ecommerce.md` quando existir. Regra base: prova de produto, estoque, frete, devolucao e checkout coerentes.

## Antes de declarar entrega

1. Rode `docs/checklists.md` sobre a versao final publicada, nao sobre o codigo que voce acha que escreveu.
2. Preencha `templates/checklist-entrega.md` com marcas reais. Pendencias nao resolvidas vao registradas com responsavel e proximo passo, nao ignoradas.
3. Adicione a nova pagina ao indice em `previews/index.html`.

## O que nao fazer

- Nao pular gates para acelerar entrega.
- Nao copiar uma referencia inteira — o repertorio orienta composicao, ritmo, tipografia e densidade; nao clona layout.
- Nao entregar apenas HTML sem os artefatos de decisao (briefing, wireframe, mapa visual, mapa de icones quando aplicavel, checklist preenchidos).
- Nao escolher icone pelo nome. Renderizar e olhar a 32px e obrigatorio — `joints-outline` desenha um joelho, `cervical` retorna colo do utero.
- Nao mover regra obrigatoria para dentro de texto de referencia estetica.
- Nao substituir o token base por preferencia estetica sem justificativa.
