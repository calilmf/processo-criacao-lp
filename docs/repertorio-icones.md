# Repertório de Ícones

Escolher ícone de card é uma decisão **visual**. Este documento existe porque tratá-la como decisão textual já produziu, numa LP de ortopedia real, um ícone de pulso cardíaco num card de coluna, um ícone de joelho num card de coluna, e um cadeado de segurança num card de sintoma.

## A regra

**Nenhum ícone é aprovado sem ter sido renderizado e olhado, no tamanho real de uso.**

Escolher pelo nome não funciona, e não é questão de procurar melhor. Dois casos reais, ambos invisíveis numa lista de texto:

- `healthicons:joints-outline` se chama "joints" e **desenha um joelho**. Foi parar em "Articulações da coluna".
- Buscar `cervical` retorna **colo do útero** e **gravata**. Em inglês médico, "cervical" não é pescoço.

Nenhuma revisão de nomes, por mais caprichada, pega isso.

## Método, por card

### 1. Descrever o que o card significa

Uma frase curta, antes de buscar. "Crises recorrentes" numa página de coluna = *piora recorrente de dor na coluna*, não "algo que pareça um alerta".

### 2. Colher vários candidatos, de toda a base

`ferramentas/harvest-candidatos.py` busca em **toda a Iconify (215 sets, ~308 mil ícones)** a partir de uma lista de termos por card, filtra sets multicoloridos/emoji/marca, e baixa ~10 candidatos por card.

Use vários termos por card, incluindo o termo clínico e o termo leigo. Limitar a busca a poucos sets conhecidos foi justamente o que escondeu, numa LP de ortopedia, que existiam `game-icons:knee-cap`, `streamline-ultimate:medical-specialty-knee-1` e `hugeicons:back-muscle-body`.

### 3. Renderizar e olhar

`ferramentas/contact-sheet.py` monta um grid com cada candidato a **32px (tamanho real) e 96px**, ao lado do título do card.

Critério, por ícone: *olhando só o desenho, sem ler o título, dá pra dizer que parte do corpo/órgão é e qual é o problema?*

O 32px é o que decide. Ícone que só funciona grande não serve.

### 4. Escolher, e checar a página inteira

Sem repetir o mesmo ícone em dois cards da mesma página — nem dentro de uma seção, nem entre seções.

Quando o conceito não tem ícone literal em lugar nenhum — confirmado por busca, não por suposição — use o ícone anatômico mais próximo **da mesma região do corpo**, nunca um de outra especialidade nem uma forma abstrata "que transmite a ideia". Registre a busca vazia como evidência.

## Organização por região

Uma pasta por região/agrupamento, um arquivo por card, nomeado pelo slug do título do card:

```
assets/topic-icons/
  coluna/dor-lombar-persistente.svg
  joelho/lesoes-de-menisco.svg
  ...
```

Isso transforma "o ícone tem que ser da região certa" em regra mecânica: **card da página `X` só pode usar ícone de `X/`**. Um ícone de joelho numa página de coluna passa a ser estruturalmente impossível, em vez de depender de alguém notar.

O agrupamento varia por especialidade — em ortopedia é região do corpo; em ginecologia pode ser fase da vida ou procedimento; em cardiologia, estrutura ou exame. O que não varia é a regra de pasta.

## Não desenhar à mão

Já foi tentado, com spec de traço, e o resultado foi pior que a biblioteca: desenho amador não sustenta uma LP de cliente. Ícone de card vem de biblioteca validada. O esforço vai para a **escolha**, não para o traço.

## Onde isso entra no processo

Fase de Copy (`docs/processo-de-criacao.md`), registrado em `templates/mapa-icones.md`, com o gate em `docs/checklists.md`.
