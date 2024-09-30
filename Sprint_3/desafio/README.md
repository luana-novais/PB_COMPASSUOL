# Etapas 
 O desafio proposto visava praticar conceitos de Python, utilizando bibliotecas como Pandas e Matplotlib para processamento e visualização de dados. O objetivo principal era ler um arquivo de estatísticas da loja de aplicativos, realizar operações de limpeza e manipulação dos dados, e gerar gráficos que facilitassem a compreensão das informações. Todas as etapas que vou listar a baixo, pode ser observada no arquivo [RESOLUÇÃO DESAFIO](./desafio2.ipynb)

 #### Etapa 1: Preparação do Ambiente
Antes de começar o desenvolvimento, realizei a instalação das bibliotecas que usaria durante o desenvolvimento, utilizei o comando ``pip install pandas matplotlib``
Também instalei a extenção do Jupyther no vs Code. 

#### Etapa 2: Desenvolvimento e Análise

###### Leitura do Arquivo CSV e Remoção de Linhas Duplicadas
Iniciei o projeto lendo o arquivo googleplaystore.csv, utiilzando a biblioteca Pandas e verificando as primeiras linhas e dimensões do dataset. Também realizei a limpeza dos dados retirando as linhas duplicadas. Usei os comandos: 
- ``read_csv`` : abrir o arquivo .csv
- ``drop_duplicates(subset='App')``: remover as linhas duplicadas se baseando na coluna do nome do App. 

###### Gráfico de Barras: Top 5 Apps por Número de Instalação
Em seguida, gerei um gráfico de barras para mostrar os 5 aplicativos mais instalados. Primeiro, ordenei os dados pelo número de instalações, nessa hora teve um problema na coluna installs, na linha 10472, a caluna Category estava sem o valor, o que causou um deslocamento do valor free que deveria estar na coluna Type. 
Para resolver o problema defini uma váriavel para verificar se o valor Free aparecia em alguma linha, converti a coluna Install para o tipo object e depois fiz o realinhamento das colunas. 

    - O valor da coluna Current Ver é movido para Android Ver.
    - O valor de Last Updated vai para Current Ver.
    - O valor de Genres vai para Last Updated.
    - O valor de Content Rating vai para Genres.
    - O valor de Price vai para Content Rating.
    - O valor de Type vai para Price.
    - O valor "Free" (que estava em Installs) é movido para Type.
    - O valor que estava em Size é movido para Installs.
    - O valor que estava em Reviews é movido para Size.
    - A coluna Category recebe um valor nulo, já que nesse caso não há uma categoria válida para apps que são listados como "Free".

Depois de realinhar as colunas, usei o replace para retirar os caracteres indesejados, como virgula e o simbolo +, por fim converti a coluna para valor númerico. 
Com os dados todos tratados, ordenei os dados pelo número de instalações e selecionei os top 5 e criei o gráfico de barras com o resultado.

![](/Sprint_3/evidencias/top-5-app.png)

###### Gráfico de Pizza: Categorias de Apps
Para visualizar a distribuição das categorias de aplicativos, gerei um gráfico de pizza. Contabilizei a frequência das categorias e, em seguida, utilizei Matplotlib para criar o gráfico:
![](/Sprint_3/evidencias/categoria-app.png)

###### App mais Caro
Realizei o cálculo do aplicativo mais caro na Play Store. Isso foi feito limpando a coluna Price, removendo os símbolos de dólar e convertendo os valores para o tipo float. Depois, selecionei o app com o maior preço. 
O app mais caro é I'm Rich - Trump Edition  400.0

###### Número de Apps Classificados como 'Mature 17+'
Para verificar quantos apps eram classificados como "Mature 17+", criei um DataFrame filtrado onde a coluna 'Content Rating' é igual a 'Mature 17+'. Ou seja, ele seleciona apenas as linhas onde o conteúdo do aplicativo é classificado para pessoas com 17 anos ou mais.

###### Top 10 Apps por Número de Reviews
Primeiramente fiz a conversão da coluna Reviews para o tipo númerico. A função pd.to_numeric() converte valores que podem estar no formato de string (ou outro formato) em números.
Para encontrar os 10 app com o maior número de avaliações, utilizei o método nlargest() retorna as 10 maiores linhas do DataFrame com base na coluna 'Reviews'. 

###### Gênero Mais Popular de Apps
O desafio pedia para criar dois novos calculos, primeiro decidi mostrar qual era o gênero que mais aparecia no dataframe. Utilizei os comandos:  
- ``df.groupby('Genres')``: Agrupa os dados da coluna 'Genres', que contém os gêneros dos aplicativos.
- ``['App'].count()``: Conta o número de aplicativos ('App') em cada grupo (gênero).
- ``.reset_index(name='Contagem')``: Cria um DataFrame a partir do resultado, atribuindo o nome 'Contagem' à nova coluna que contém o número de aplicativos por gênero.

Depois ordenei a coluna contagem em ordem decrescente e usei o head(1) para retornar a primeira linha, representando o gênero mais popular. 

O desafio também pedia para apresentar 2 gráficos diferentes dos que já foram apresentados acima, decidi utilizar o gráfico de radar é ótimo para comparar várias variáveis em relação a um ponto central comum. Para o caso dos gêneros de aplicativos e suas contagens, podemos usar um gráfico de radar para mostrar como diferentes gêneros se comparam entre si, ficando fácil observar qual o app que mais apareceu no DataFrame. 

![](/Sprint_3/evidencias/app-genero.png)

###### Análise dos Top 10 Jogos por Instalações
O segundo calculo escolhido foi para representar os 10 app com mais instalação dentro do categoria Games, filtrei todos os aplicativos da categoria "GAME", ordena-os pelo número de instalações e selecionei os 10 jogos mais baixados.
O segundo gráfico escolhido, foi o grafico de linhas, que permite uma comparação direta entre os jogos. As linhas conectam os pontos de dados, permitindo que o espectador observe rapidamente as diferenças no número de downloads entre os jogos.
Este código irá gerar um gráfico de linhas mostrando os 10 jogos mais baixados, permitindo visualizar a comparação entre o número de instalações para cada jogo.  ele permite visualizar claramente a relação entre os jogos e o número de instalações, facilitando a identificação de qual jogo se destaca em popularidade.

![](/Sprint_3/evidencias/top-games.png)