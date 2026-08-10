# Privacidade e Consentimento

Este documento define o minimo de privacidade para Landing Pages criadas pela Pulso. Ele e um padrao operacional, nao substitui validacao juridica ou contratual para cada cliente.

## Principio: a responsabilidade nao e presumida

Antes do build, registrar no briefing:

- quem e o **controlador** dos dados coletados na LP;
- qual e o papel da Pulso naquele projeto (controladora, operadora ou ambas em atividades distintas);
- canal de contato para pedidos de privacidade;
- destino do CTA e quais dados o visitante pode informar;
- tecnologias carregadas (GTM, Google Ads, GA4, Meta Pixel, Clarity, CRM, bridge de WhatsApp etc.);
- URL da politica de privacidade e, quando aplicavel, do aviso complementar do cliente.

Em LPs de captacao de consulta, o profissional ou consultorio normalmente decide a finalidade do atendimento e dos leads. Isso nao deve ser assumido: confirmar com o cliente e com o contrato. A Pulso pode tratar dados sob instrucao do cliente ou decidir sobre dados das suas proprias operacoes de marketing; registre a funcao real em vez de usar um rotulo generico.

## Politica central da Pulso: quando usar

Uma politica central da Pulso pode padronizar informacoes sobre a infraestrutura comum, como hospedagem, tag manager, cookies, medicao de campanhas e bridge de agendamento. Ela deve descrever somente o que a Pulso realmente opera e manter canal de contato proprio.

Ela **nao substitui** a transparencia sobre o atendimento do cliente. Cada LP deve, no minimo:

1. identificar de forma clara o controlador do contato/agendamento;
2. exibir link para a politica central da Pulso quando ela cobrir as tecnologias usadas;
3. adicionar aviso ou politica complementar do cliente quando ele tratar dados para atendimento, prontuario, CRM ou outros fins proprios;
4. evitar prometer que dados nao sao compartilhados quando ha fornecedores, bridge ou ferramentas de medicao envolvidos.

## Conteudo minimo do aviso aplicavel a cada LP

- identificacao e canal de contato do controlador;
- categorias de dados tratadas na navegacao e no contato;
- finalidades do tratamento e destino do CTA;
- tecnologias de terceiros e categorias de cookies;
- como o visitante altera preferencias de cookies;
- compartilhamentos necessarios com fornecedores e canais de agendamento;
- direitos do titular e como solicitar atendimento;
- data da ultima atualizacao.

Nao declarar "legitimo interesse" como justificativa de publicidade ou remarketing por conveniencia. A definicao de bases legais deve ser validada pelo controlador.

## Consentimento e tracking

Para LPs com Ads ou tecnologias de medicao/publicidade:

- registrar o estado de consentimento antes do primeiro carregamento das tags;
- manter essenciais separados de medicao e publicidade;
- oferecer "aceitar todos" e "usar apenas essenciais", sem consentimento implicito;
- persistir a escolha de modo versionado e permitir reabri-la pela politica;
- configurar controles proprios de terceiros fora do Consent Mode nativo;
- testar eventos e requests antes de ativar campanha.

Consulte `specs/google-ads.md` para a implementacao tecnica de GTM e Consent Mode v2.

## Gate de publicacao

Uma LP com coleta de dados ou tracking nao esta pronta para Ads se faltar qualquer um dos itens abaixo:

- controlador, canal de privacidade ou URL de politica confirmados;
- destino do CTA/bridge definido;
- banner e preferencias funcionando;
- Consent Mode e eventos validados, quando houver tags;
- pendencias de privacidade registradas com responsavel e proximo passo.
