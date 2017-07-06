# Defesa do Samuel - 20170529

## Correcoes de Forma

- (OK) a capa est� errada com a data de defesa e dep�sito, a lista de abrevia��es tem defini��es, refer�ncias bibliogr�ficas precisam ser padronizadas, nossos nomes (Cesar sem acento, Claudio).
Erro no nome do Claudio e no meu
- (OK) formato de cole��o de artigos: deixar no come�o de cada cap�tulo que o conte�do vem do artigo correspondente. footnote no in�cio de cada cap�tulo.
Existe alguma coisa muito diferente do texto original? Em rela��o aos papers. Se isso aconteceu, precisa deixar claro. Assim como mencionar� que cada cap 2 e 3 saiu dos papers x e y, etc.
refazer a conclus�o para n�o deixar parte do texto de nenhum artigo. tirar o termo ongoing work.
- (OK) trazer o ap�ndice para o cap 2, contextualizar. +extra: arrumar titulos das tabelas
- (OK) N�o deveria deixar nome de usu�rio aparececendo.
- (OK) extra: Modificacoes para deposito no comeco da tese, banca de defesa
- (OK - removi a lista, nao achei no template aprovado pela CPG uma lista de acronimos ou definicoes para mover os itens relevantes para la https://www.ime.usp.br/dcc/pos/normas/tesesedissertacoes) lista de acr�nimos, abrevia��es (tem coisa l� que n�o � abrevia��o)
- (? - Nao sei bem o q fazer aqui) Formato, autoriza��o dos co-autores
- (OK) Tirar o termo estudar.


## Correcoes de Conteudo - MINOR - 1/2h each

- INTRO:
	- Fabricio: faltou motiva��o na introdu��o para os dois trabalhos, twitter e reddit. Jesus: Faltou uma melhor contextualiza��o no cap�tulo 1. Aproveitar os coment�rios da argui��o para tentar responder ao m�ximo e deixar claro na pr�pria introdu��o (motiva��o, background...). objetivos: deixar mais claros, falar de objetivos  espec�ficos. Luc: a intro precisa deixar claro: por que os objetivos da tese levaram �s contribui��es dos cap�tulos 2 e 3. 
	- A apresenta��o dos slides deixou uma passagem mais suave. aproveitar a intro dos slides / apresenta��o da defesa na intro da tese
	- pergunta: qual �rea de computa��o sua contribui��o reside? computational social science de Cornell.
	- Mencionar sua atua��o atual, getninjas, projeto PIPE FAPESP
- Documentar que Proposal of the problem of studying users' indirect reactions. � uma contribui��o, que ningu�m percebeu. citar as refs.
- Complexidade computacional dos m�todos empregados na an�lise. falar sobre esse t�pico em uma se��o espec�fica na conclus�o. falar da import�ncia do big query etc. 
- fig 3.5 e descontinuidade, analisar e explicar melhor.
- enfatizar melhor como  a fig 2.6 explica grande parte das quest�es levantadas.
- ferramentas para an�lise: o que vc desenvolveu? o que vc usou pronto? indicar isso nos materiais e m�todos de cada cap 2, 3. Algo pode ser compartilhado, disponibilizado?
- explicar como foi feita a conta dos 11pct da tabela 2.6.

## Correcoes de Conteudo - MAJOR

- Definicoes e metodos em geral: Fab: pg 10: qual a motiva��o para o tf-idf? comentar um pouco no texto. Comentar a modifica��o por vc criada. Jesus: complementar sobre conceitos b�sicos, tf-idf, precision  recall, redu��o � raiz, retirada de plural, etc. faltou defini��o de conceitos importantes, como tf-idf, ego-network, fazer isso em uma se��o espec�fica no in�cio de cada cap�tulo 2, 3, formalizar o que � uma rea��o impl�cita / expl�cita. Termo normalized tf idf. Precisa definir. na def das m�tricas, � importante deixar claro 0 � ruim?1 � o m�ximo e melhor? a m�trica captura bem o retweet e o esfor�o
- Conex�o com com 2 trabalhos, Taxidou, qual a diferen�a dos trabalhos anteriores com a proposta da sua tese? Deixar isso claro. 
- conclus�o, falar de future work: registrar as grandes ideias que vc gostaria de ter feito e n�o fez.
- Fab: faltou apresentar os datasets com clareza, criar se��o espec�fica e uma tabela resumindo as principais caracter�sticas dos datasets, caracter�sticas, datas de in�cio e fim, n�mero de amostras, n�mero de classes, retweets, replies, vamos criar uma tabela com formato espec�fico e semelhante para ambos cap�tulos. Luc: melhorar a intro, incluir se��o de conceitos b�sicos, falar da escolha das redes, detalhamento de conjuntos de dados usados. a an�lise do twitter n�o tinha dado de entrada dos users na rede? a tab 2.4 n�o tem informa��o sobre ego-networks. Acrescentar.

## Future work

- Poder�amos usar outras m�dias (informa��es n�o textuais, imagem, etc) na an�lise do tweeter? mencionar em trabalhos futuros. separar a dicuss�o conceitual da implementa��o. o m�todo poderia ser usado na an�lise de outros microblogs?
- limita��es: o fato que usamos conjto de dados de pol�tica pode afetar o resultado?
- existe alguma caracter�stica que permita prever se um usu�rio novo vai viver bastante, ser� ativo? conex�o com sele��o de caracter�sticas para modelar o problema de quem vai viver na rede, quem vai ser ativo, etc. Vamos mencionar como trabalhos futuros.
- trabalho futuro: como a comunidade influencia os usu�rios no momento que novatos nela se iniciam.
- trabalho futuro: predi��o
- trabalhos futuros: considerar 100 �ltimos similares, ao inv�s de apenas os 100 �timos. Claudio: quest�o dos 100 tweets
- aplica��o em botnet e fake news

## Questoes que requerem novos testes ou reescrita extensa do texto - NOT DOING

- na intro: ...diferen�as dos trabalhos do estado da  arte, trabalho da Taxidou, etc)
- usar a mediana, pois a m�dia pode n�o fazer tanto sentido. precisa discutir qu�o robusta � a conclus�o. Fab: incluir gr�ficos da normaliza��o, slide Next Steps, e discutir o impacto nas conclus�es. como validar os 11pct? foi feito implicitamente.  discutir como isso poderia ser feito.
- pg 13: como o cut-off foi definido? por que usar a m�dia? podia usar um teste de hip�tese para verificar como o resultado depende do cut-off? Claudio: quest�o da robustez do threshold 0.384
- qu�o dependente s�o os resultados da medida de similaridade usada? mencionar a dist�ncia de edi��o de Jaro. citar e comentar.
- Jesus: quest�o sobre #hashtags, nomes de usu�rios. Isso � retirado ou mantido na an�lise? O que aconteceria se retirar? Seria poss�vel retirar e verificar sua hip�tese experimentalmente? Conseguimos fazer algum experimento assim? Luc: por que a m�trica n�o chega a 1 no retweet? retomar as sugest�es do Jesus, tirar hash, etc.
- muita mistura de m�todos, dados, resultados (conclus�es da an�lise). Separar bem essas 3 coisas. reorganizar a conclus�o, diminuindo seu tamanho e facilitando a compreens�o para o leitor.
- a janela � definida em 82pct. O que acontece se aumentar?
- cap�tulo 3 apresenta hip�teses e pesquisa que da� decorre. O cap�tulo 2 precisa ter isso.
