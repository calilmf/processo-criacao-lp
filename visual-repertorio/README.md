# Repertorio Visual

Referencias esteticas organizadas como material recuperavel por decisao, nao por plataforma de origem. Ver `docs/repertorio-visual.md` para o principio completo.

## Estrutura atual

```text
visual-repertorio/
  03-cartoes-referencia/    analise pronta para uso
  09-indices/               entrada por secao
  _templates/               modelo de cartao
```

Pastas mencionadas na doc (`00-taxonomia`, `01-fontes`, `02-referencias-brutas`, `04-padroes-por-secao`, `05-componentes`, `06-lookbooks`, `07-receitas-combinatorias`) serao criadas quando surgir material real para elas.

## Como usar durante um projeto

1. Abra `09-indices/por-secao.md`.
2. Escolha 1 a 3 cartoes por secao — leia inteiros, inclusive a sessao de riscos.
3. Registre os IDs (`ref.visual.xxx`) no `templates/visual-map.md`.
4. Construa uma interpretacao original. Nao copie a referencia inteira.

## Como adicionar um cartao

1. Copie `_templates/cartao-referencia.md`.
2. Nome do arquivo em dashes: `{fonte}-{recorte}-{tom}.md`. Ex: `linear-hero-editorial-serifado.md`.
3. ID interno em dots: `ref.visual.linear.hero-editorial-serifado`.
4. Preencha todos os campos, especialmente riscos e restricoes.
5. Adicione o ID no `09-indices/por-secao.md` sob a secao aplicavel.
