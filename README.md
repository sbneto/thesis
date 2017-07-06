# Defesa do Samuel - 20170529

## Correcoes de Forma

- (OK) a capa está errada com a data de defesa e depósito, a lista de abreviações tem definições, referências bibliográficas precisam ser padronizadas, nossos nomes (Cesar sem acento, Claudio).
Erro no nome do Claudio e no meu
- (OK) formato de coleção de artigos: deixar no começo de cada capítulo que o conteúdo vem do artigo correspondente. footnote no início de cada capítulo.
Existe alguma coisa muito diferente do texto original? Em relação aos papers. Se isso aconteceu, precisa deixar claro. Assim como mencionará que cada cap 2 e 3 saiu dos papers x e y, etc.
refazer a conclusão para não deixar parte do texto de nenhum artigo. tirar o termo ongoing work.
- (OK) trazer o apêndice para o cap 2, contextualizar. +extra: arrumar titulos das tabelas
- (OK) Não deveria deixar nome de usuário aparececendo.
- (OK) extra: Modificacoes para deposito no comeco da tese, banca de defesa
- (OK - removi a lista, nao achei no template aprovado pela CPG uma lista de acronimos ou definicoes para mover os itens relevantes para la https://www.ime.usp.br/dcc/pos/normas/tesesedissertacoes) lista de acrônimos, abreviações (tem coisa lá que não é abreviação)
- (? - Nao sei bem o q fazer aqui) Formato, autorização dos co-autores
- (OK) Tirar o termo estudar.


## Correcoes de Conteudo - MINOR - 1/2h each

- INTRO:
	- Fabricio: faltou motivação na introdução para os dois trabalhos, twitter e reddit. Jesus: Faltou uma melhor contextualização no capítulo 1. Aproveitar os comentários da arguição para tentar responder ao máximo e deixar claro na própria introdução (motivação, background...). objetivos: deixar mais claros, falar de objetivos  específicos. Luc: a intro precisa deixar claro: por que os objetivos da tese levaram às contribuições dos capítulos 2 e 3. 
	- A apresentação dos slides deixou uma passagem mais suave. aproveitar a intro dos slides / apresentação da defesa na intro da tese
	- pergunta: qual área de computação sua contribuição reside? computational social science de Cornell.
	- Mencionar sua atuação atual, getninjas, projeto PIPE FAPESP
- Documentar que Proposal of the problem of studying users' indirect reactions. é uma contribuição, que ninguém percebeu. citar as refs.
- Complexidade computacional dos métodos empregados na análise. falar sobre esse tópico em uma seção específica na conclusão. falar da importância do big query etc. 
- fig 3.5 e descontinuidade, analisar e explicar melhor.
- enfatizar melhor como  a fig 2.6 explica grande parte das questões levantadas.
- ferramentas para análise: o que vc desenvolveu? o que vc usou pronto? indicar isso nos materiais e métodos de cada cap 2, 3. Algo pode ser compartilhado, disponibilizado?
- explicar como foi feita a conta dos 11pct da tabela 2.6.

## Correcoes de Conteudo - MAJOR

- Definicoes e metodos em geral: Fab: pg 10: qual a motivação para o tf-idf? comentar um pouco no texto. Comentar a modificação por vc criada. Jesus: complementar sobre conceitos básicos, tf-idf, precision  recall, redução à raiz, retirada de plural, etc. faltou definição de conceitos importantes, como tf-idf, ego-network, fazer isso em uma seção específica no início de cada capítulo 2, 3, formalizar o que é uma reação implícita / explícita. Termo normalized tf idf. Precisa definir. na def das métricas, é importante deixar claro 0 é ruim?1 é o máximo e melhor? a métrica captura bem o retweet e o esforço
- Conexão com com 2 trabalhos, Taxidou, qual a diferença dos trabalhos anteriores com a proposta da sua tese? Deixar isso claro. 
- conclusão, falar de future work: registrar as grandes ideias que vc gostaria de ter feito e não fez.
- Fab: faltou apresentar os datasets com clareza, criar seção específica e uma tabela resumindo as principais características dos datasets, características, datas de início e fim, número de amostras, número de classes, retweets, replies, vamos criar uma tabela com formato específico e semelhante para ambos capítulos. Luc: melhorar a intro, incluir seção de conceitos básicos, falar da escolha das redes, detalhamento de conjuntos de dados usados. a análise do twitter não tinha dado de entrada dos users na rede? a tab 2.4 não tem informação sobre ego-networks. Acrescentar.

## Future work

- Poderíamos usar outras mídias (informações não textuais, imagem, etc) na análise do tweeter? mencionar em trabalhos futuros. separar a dicussão conceitual da implementação. o método poderia ser usado na análise de outros microblogs?
- limitações: o fato que usamos conjto de dados de política pode afetar o resultado?
- existe alguma característica que permita prever se um usuário novo vai viver bastante, será ativo? conexão com seleção de características para modelar o problema de quem vai viver na rede, quem vai ser ativo, etc. Vamos mencionar como trabalhos futuros.
- trabalho futuro: como a comunidade influencia os usuários no momento que novatos nela se iniciam.
- trabalho futuro: predição
- trabalhos futuros: considerar 100 últimos similares, ao invés de apenas os 100 útimos. Claudio: questão dos 100 tweets
- aplicação em botnet e fake news

## Questoes que requerem novos testes ou reescrita extensa do texto - NOT DOING

- na intro: ...diferenças dos trabalhos do estado da  arte, trabalho da Taxidou, etc)
- usar a mediana, pois a média pode não fazer tanto sentido. precisa discutir quão robusta é a conclusão. Fab: incluir gráficos da normalização, slide Next Steps, e discutir o impacto nas conclusões. como validar os 11pct? foi feito implicitamente.  discutir como isso poderia ser feito.
- pg 13: como o cut-off foi definido? por que usar a média? podia usar um teste de hipótese para verificar como o resultado depende do cut-off? Claudio: questão da robustez do threshold 0.384
- quão dependente são os resultados da medida de similaridade usada? mencionar a distância de edição de Jaro. citar e comentar.
- Jesus: questão sobre #hashtags, nomes de usuários. Isso é retirado ou mantido na análise? O que aconteceria se retirar? Seria possível retirar e verificar sua hipótese experimentalmente? Conseguimos fazer algum experimento assim? Luc: por que a métrica não chega a 1 no retweet? retomar as sugestões do Jesus, tirar hash, etc.
- muita mistura de métodos, dados, resultados (conclusões da análise). Separar bem essas 3 coisas. reorganizar a conclusão, diminuindo seu tamanho e facilitando a compreensão para o leitor.
- a janela é definida em 82pct. O que acontece se aumentar?
- capítulo 3 apresenta hipóteses e pesquisa que daí decorre. O capítulo 2 precisa ter isso.
