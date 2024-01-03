Questão 1 – Cadastro de jogos [valor: 4]
Cada jogo deve ser cadastrado com as seguintes informações:
-Código
-Título
-Console (XBox, PlayStation, Switch, PC)
-Gênero (Ação, Aventura, Estratégia, RPG, Esporte, Simulação)
-Preço (valor maior que zero e valor menor ou igual a 500)
-Avaliações
Seu programa deve exibir um formulário com cinco campos de texto – um para cada atributo do jogo, com
exceção de Avaliações. Você deve usar Exceptions para validar os campos, de acordo com as opções
permitidas. O formulário de cadastramento não deve exibir o campo Avaliações, já que a avaliação do
jogo deve ser feita posteriormente.
Questão 2 – Avaliação de jogos [valor: 2]
Seu programa deve permitir a avaliação de cada jogo por meio de estrelas (notas de 1 a 5). Deve ser
possível avaliar um jogo quantas vezes quiser. Para tanto, deve existir a opção Avaliar no menu Jogo. Ao
selecionar essa opção, deve-se exibir uma tela contendo um campo de texto para digitação do código do
jogo e um combo box com 5 opções: 1 estrela, 2 estrelas .... até 5 estrelas. A avaliação deve ser guardada
na lista de avaliações de forma a permitir o cálculo da avaliação do jogo posteriormente. Note: o que deve
ser guardado é um número entre 1 e 5.
Questão 3 – Consulta de jogos [valor: 4]
Seu programa deve prover um mecanismo de consulta que permita selecionar jogos por Avaliação
(número de estrelas). Para tanto, você deve construir uma interface com um combo box contendo as 5
opções de estrelas (1 estrela, 2 estrelas .... 5 estrelas). Ao selecionar 1 estrela, deve-se mostrar todos os
jogos cuja avaliação é 1 estrela, e assim sucessivamente até 5 estrelas. Para determinar a avaliação
média de um jogo deve-se somar todas as suas avaliações individuais e dividir pelo número de avaliações
do jogo. Assim, se um jogo teve as seguintes avaliações: 2 – 4 – 4 – 5, temos 2+4+4+5=15, 15/4 = 3,75,
então este jogo é um jogo 4 estrelas, pois deve-se levar em conta o seguinte:
0 <= média <= 1 equivale a 1 estrela
1 < média <= 2 equivale a 2 estrelas
2 < média <= 3 equivale a 3 estrelas
3 < média <= 4 equivale a 4 estrelas
4 < média <= 5 equivale a 5 estrelas
Assim, ao selecionar 3 estrelas no combo box, deve-se exibir os dados de todos os jogos que tenham
classificação 3 estrelas. O mesmo vale para as demais estrelas. Jogos que não tiveram nenhuma
avaliação devem ser desconsiderados na hora da consulta.
---------
Todos os dados devem ser persistidos em arquivo.
Sugere-se criar o menu Jogo com as opções Cadastrar, Avaliar e Consultar.
