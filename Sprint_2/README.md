# Sprint 2

#### SQL para análise de dados
Na sprint 2 aprendemos sobre operações em bases de dados. Tais bases residem em Sistemas Gerenciadores de Banco de Dados (SGBDs), boa parte sendo relacional. Para estes, utilizamos a linguagem SQL para executar as operações. SQL é uma ferramenta poderosa para análise de dados, permitindo extrair, transformar e visualizar informações de grandes bancos de dados. Para análises de dados, o SQL oferece vários recursos úteis como consultas Básicas, agregação de dados, junções de tabelas (JOINs), subconsultas e CTEs. Alguns dos comandos aprendidos foi:
    - ``SELECT``: utilizado para consultar e recuperar dados de uma ou mais tabelas no banco de dados.
    - ``FROM``: especifica a tabela ou tabelas de onde os dados serão recuperados.
    - ``WHERE``: aplica uma condição para filtrar os registros retornados pela consulta. 
    - ``ORDER BY``: utilizado para ordenar os resultados da consulta com base em uma ou mais colunas, em ordem ascendente ou descendente.
    - ``INNER JOIN``: combina registros de duas ou mais tabelas com base em uma condição de correspondência, retornando apenas os registros que têm correspondência em ambas as tabelas. 
    - ``LEFT JOIN``: etorna todos os registros da tabela à esquerda e os registros correspondentes da tabela à direita.
    - ``GROUP BY``: agrupa registros que têm valores iguais em uma ou mais colunas.
<br>

#### Modelo Relacional
O modelo relacional organiza os dados em tabelas (também chamadas de relações), onde cada tabela possui linhas e colunas. Cada linha é um registro e cada coluna é um atributo. As tabelas são interligadas por relacionamentos, através de chaves primárias (um identificador único em uma tabela) e chaves estrangeiras (referências à chave primária de outra tabela). Exemplo: Uma tabela de clientes pode ter uma coluna "ID do cliente" como chave primária, e uma tabela de pedidos pode usar "ID do cliente" como chave estrangeira para associar um pedido ao cliente correto.

- Tabelas: Cada tabela no modelo relacional representa uma entidade, como Clientes ou Produtos.
- Chaves Primárias: São usadas para identificar de maneira única cada registro dentro de uma tabela.
- Chaves Estrangeiras: Estabelecem relacionamentos entre diferentes tabelas, referenciando a chave primária de outra tabela.
- Normalização: É o processo de organizar os dados para evitar redundâncias e garantir a integridade dos dados, dividindo dados em várias tabelas relacionadas.
 - SQL: A linguagem padrão utilizada para manipular e consultar dados em um banco de dados relacional.
<br>

##### Normalização
A normalização é o processo de organizar os dados em um banco relacional para reduzir a redundância e melhorar a integridade dos dados. Ela é feita em várias etapas chamadas de formas normais (1ª, 2ª, 3ª forma normal, etc.).
O objetivo da normalização é evitar anomalias de inserção, atualização e exclusão, e garantir que os dados sejam armazenados de forma eficiente.
Por exemplo, se você tiver uma tabela onde informações de clientes e de pedidos estão juntas. Para normalizar, você poderia dividir essa tabela em duas, uma contendo as informações de clientes e outra com os pedidos, utilizando chaves estrangeiras para conectar as tabelas.
A normalização ajuda a criar estruturas de dados eficientes e consistentes em bancos de dados relacionais, eliminando redundâncias e facilitando a manutenção dos dados ao longo do tempo. Cada forma normal adiciona um nível de organização mais refinado, permitindo um maior controle sobre as dependências e a integridade dos dados.
- **Primeira forma normal(1NF):** Na Primeira Forma Normal (1FN), tratamos as repetições e garantimos que os atributos sejam armazenados de forma única, ou seja, não deve haver nenhum outro atributo com valores duplicados na mesma linha da tabela.
- **Segunda forma normal(2NF):** focamos na eliminação de redundâncias nas tabelas, assegurando que todos os atributos dependam completamente da chave primária. Os atributos que não dependem ou dependem parcialmente da chave primária são movidos para outra tabela, estabelecendo uma relação clara com a chave primária da tabela original.
- **Terceira forma normal(3NF):** organizamos os atributos que dependem uns dos outros, mas que não são chaves (primárias ou estrangeiras). Se necessário, criamos uma tabela adicional para reestruturar a relação de dependência entre esses atributos. Essas tabelas secundárias devem incluir uma chave primária ou estrangeira.


#### Modelo Dimensional
A Modelagem Dimensional é uma técnica de criação e visualização de modelos de dados geralmente utilizada na construção de Data Warehouses. Esse modelo é composto por um conjunto de medidas que descrevem aspectos comuns de negócios. Comparado ao Modelo Relacional, o modelo dimensional é mais simples, mais expressivo e mais fácil de entender. É utilizado principalmente para consultas e relatórios, onde é importante ter uma estrutura que permita fácil navegação e agregação dos dados

O modelo traz benefícios como: 
    - Facilidade na interação com o usuário final.
    - Melhora a compreensão dos processos de negócios.
    - Aumenta a rapidez nas consultas de dados.

O MD possui dois componentes, a tabela fato que representa as métricas quantitativas que são analisadas, como vendas ou receitas, e são armazenados em tabelas de fatos. E a tabela Dimensão que fornece o contexto para os fatos. Representam as diferentes perspectivas ou categorias para análise, como tempo, produto ou cliente, e são armazenadas em tabelas de dimensões.
Por exemplo, em uma análise de vendas, a tabela fato pode conter informações como "quantidade vendida" e "valor total", enquanto as tabelas dimensão podem ter dados como "produto", "cliente" e "data".

Os principais tipos de modelagem dimensional são:

- Modelo em Estrela: Consiste em uma tabela de fato centralizada, conectada a várias tabelas de dimensões. Essa estrutura facilita consultas, oferecendo um design simples e intuitivo.
- Modelo em Floco de Neve: É uma estrutura onde a tabela de fato é associada a tabelas de dimensões que podem, por sua vez, estar relacionadas a outras tabelas de dimensões. Esse modelo reflete uma abordagem mais normalizada e pode se assemelhar ao modelo relacional dentro do Data Warehouse.


# Exercícios
Nessa sprint foi proposto 2 casos de estudos, totalizando 16 exercícios no total. Abaixo tem a resolução de cada um:
- Caso de estudo Biblioteca:
    - E01: apresentar todos os livros publicados após 2014
    [RESOLUÇÃO E01](/Sprint_2/exercicios/exercicio-1.sql)
    - E02: mostrar os 10 livros mais caros
    [RESOLUÇÃO E02](/Sprint_2/exercicios/exercicio-2.sql)
    - E03: quais as 5 editoras com mais livros na biblioteca
    [RESOLUÇÃO E03](/Sprint_2/exercicios/exercicio-3.sql)
    - E04: qual a quantidade de livros publicada por cada autor
    [RESOLUÇÃO E04](/Sprint_2/exercicios/exercicio-4.sql)
    - E05: apresentar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil
    [RESOLUÇÃO E05](/Sprint_2/exercicios/exercicio-5.sql)
    - E06: o autor com maior número de livros publicados
    [RESOLUÇÃO E06](/Sprint_2/exercicios/exercicio-6.sql)
    - E07: o nome dos autores com nenhuma publicação
    [RESOLUÇÃO E07](/Sprint_2/exercicios/exercicio-7.sql)
<br>

- Caso de estudo Loja:
    - E08: o código e o nome do vendedor com maior número de vendas 
    [RESOLUÇÃO E08](/Sprint_2/exercicios/exercicio-8.sql)
    - E09: o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02
    [RESOLUÇÃO E09](/Sprint_2/exercicios/exercicio-9.sql)
    - E10: calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados
    [RESOLUÇÃO E10](/Sprint_2/exercicios/exercicio-10.sql)
    - E11: o código e nome cliente com maior gasto na loja
    [RESOLUÇÃO E11](/Sprint_2/exercicios/exercicio-11.sql)
    - E12: código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero)
    [RESOLUÇÃO E12](/Sprint_2/exercicios/exercicio-12.sql)
    - listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz
    [RESOLUÇÃO E13](/Sprint_2/exercicios/exercicio-13.sql)
    - E14: o gasto médio por estado da federação
    [RESOLUÇÃO E14](/Sprint_2/exercicios/exercicio-14.sql)
    - E15: os códigos das vendas identificadas como deletadas
    [RESOLUÇÃO E15](/Sprint_2/exercicios/exercicio-15.sql)
    - E16: a quantidade média vendida de cada produto agrupado por estado da federação
    [RESOLUÇÃO E16](/Sprint_2/exercicios/exercicio-16.sql)

- Exeríicio exportação
Nesse exercício utilizei a base de dados ``biblioteca`` para realizar a  exportação de duas query, a primeira era o resultado da query que obtém os 10 livros mais caros para um arquivo ``.csv``, utilizando o caractere ``;`` como separador:
[Query 10 livros](/Sprint_2/exercicios/exercicio-exportacao.sql) [Arquivo exportado em .csv](/Sprint_2/exercicios/exercicio-exportacao.csv)
A segunda exportação era para exportar a query que obtém as 5 editoras com maior quantidade de livros, utilizando caracte ``|`` como separador:
[Query 5 editoras](/Sprint_2/exercicios/exercicio-exportacao2.sql)  [Arquivo exportado em .csv](/Sprint_2/exercicios/exercicio-exportacao2.csv)


# Certificados

# Desafio
O objetivo do desafio era colocar em prática o conhecimento sobre modelagem de dados Relacional e Dimensional com o uso de Linguagem SQL. Foi disponibilizado um arquivo com um banco de dados chamado ``consecionario.sqlite``, onde o desafio era normalizar a base de dados aplicando as formas normais e depois transformar o modelo relacional em dimensional. 

[Desafio](./desafio/README.md)

