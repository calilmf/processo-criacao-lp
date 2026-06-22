# Repertorio Visual

Referencias esteticas devem aumentar o vocabulario visual sem substituir a estrategia da Landing Page. Para isso, organize-as como material recuperavel por decisao, e nao por plataforma de origem.

## Estrutura sugerida

```text
visual-repertorio/
  00-taxonomia/                 tags, criterios e eixos visuais
  01-fontes/                    galerias e fontes de descoberta
  02-referencias-brutas/        links, capturas e primeiras observacoes
  03-cartoes-referencia/        analise pronta para uso
  04-padroes-por-secao/         hero, prova, mecanismo, FAQ, CTA etc.
  05-componentes/               cards, formularios, icones e microinteracoes
  06-lookbooks/                 combinacoes por segmento ou tom
  07-receitas-combinatorias/    combinacoes para casos frequentes
  09-indices/                   entrada por secao, tom e especialidade
  _templates/                   modelo de cartao e mapa visual
```

## Cartao de referencia

Cada referencia analisada precisa de um ID estavel, por exemplo `ref.visual.nome-da-referencia.tom`. O cartao deve dizer:

- o que torna a referencia relevante;
- em quais secoes ela funciona;
- quais elementos podem inspirar a implementacao;
- riscos de copiar ou aplicar fora de contexto;
- combinacoes sugeridas com outras referencias;
- restricoes de performance, acessibilidade ou setor.

Isso permite recuperar referencias por necessidade: "preciso de um hero com foto contextual e autoridade premium", em vez de pedir uma lista vaga de sites bonitos.

## Como usar durante o projeto

1. Entre pelo indice da secao que precisa ser desenhada.
2. Escolha de uma a tres referencias que tenham funcao complementar.
3. Leia os cartoes completos, incluindo riscos e limites.
4. Escolha um padrao de secao aplicavel.
5. Registre os IDs no mapa visual.
6. Construa uma interpretacao original da decisao.

Exemplo:

| Secao | Funcao | Referencias | Padrao | Decisao |
| --- | --- | --- | --- | --- |
| Hero | Contexto e acao inicial | `ref.visual.exemplo.editorial` + `ref.visual.exemplo.healthtech` | `pattern.hero.foto-contextual-overlay` | Foto real, hierarquia editorial e CTA com alto contraste. |

## Protecao do CTA

Referencia visual pode influenciar contraste, espacamento, acabamento e microinteracao. Ela nao pode alterar o verbo estrategico, destino, prioridade, tracking ou requisitos de formulario definidos para a pagina.

Essa separacao e importante: design decide a apresentacao da acao; estrategia decide qual acao precisa acontecer.

## O que nao colocar no repertorio

- Copy comercial de outras marcas.
- Claims medicos ou promessas de resultado de terceiros.
- Referencia sem analise de uso e risco.
- Efeito que prejudica carregamento, legibilidade ou mobile.
- Uma pagina inteira tratada como algo para copiar.
