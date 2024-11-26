# Resumo do Curso de Spark

O Apache Spark é uma poderosa ferramenta de processamento de dados distribuídos, projetada para lidar com grandes volumes de dados de forma eficiente. Ele permite realizar operações em paralelo em clusters de computadores, o que o torna ideal para cenários de Big Data. Utilizando o PySpark, que é a interface Python do Spark, podemos aproveitar a simplicidade e flexibilidade dessa linguagem para criar pipelines de dados e realizar análises avançadas.

Uma das principais características do Spark é a abstração de RDDs (Resilient Distributed Datasets), que são conjuntos de dados distribuídos, imutáveis e tolerantes a falhas. Os RDDs permitem realizar operações como mapeamento, filtragem e redução de dados em larga escala. No entanto, como a manipulação de RDDs pode ser mais técnica, o Spark introduziu os DataFrames, que oferecem uma interface de alto nível, semelhante a tabelas em bancos de dados ou a estruturas de dados como o DataFrame do Pandas no Python. Os DataFrames no PySpark facilitam muito o processamento de dados, pois permitem realizar transformações, filtragens e agregações de maneira mais intuitiva. 

Além disso, o Spark oferece o Spark SQL, um módulo que estende a funcionalidade dos DataFrames permitindo consultas em sintaxe SQL. Com ele, é possível registrar DataFrames como tabelas temporárias ou permanentes e realizar operações complexas como joins, agrupamentos e filtros usando comandos SQL tradicionais. O Spark SQL é particularmente útil para integrar equipes multidisciplinares, pois oferece uma linguagem universal para explorar e processar os dados.

Em resumo, o Spark, com o suporte do PySpark, combina a flexibilidade de trabalhar com RDDs para operações de baixo nível e o alto nível dos DataFrames para facilitar o processamento. Com o Spark SQL, ele amplia suas capacidades para permitir consultas declarativas, transformando o Spark em uma ferramenta completa para ciência de dados, análise de dados e aprendizado de máquina em escala.

# Exercícios

#### Exercício contador

Neste exercício, desenvolvi um job de processamento utilizando Spark dentro de um container Docker. Para iniciar, criei a imagem e o container necessários, depois utilizei o comando wget para baixar o arquivo ``README.md`` diretamente do repositório no GitHub. Em seguida, no Spark Shell, executei uma sequência de comandos para processar o texto e contar a frequência de ocorrência de cada palavra. O resultado da resolução está disponível na pasta [ex-contador](../Sprint_7/exercicios/ex-contador)

#### LAB Glue

Neste exercício, foi proposto processar um dataset contendo registros de nomes mais comuns nos Estados Unidos entre 1880 e 2014 utilizando o AWS Glue e PySpark. O objetivo era realizar transformações e análises nos dados, como contar registros por ano e gênero, identificar os nomes mais registrados para cada gênero e gerar estatísticas agrupadas. Além disso, foi solicitado gravar o resultado em um bucket S3 no formato JSON, particionado por gênero e ano, a resolução está disponível na pasta [LAB-Glue](../Sprint_7/exercicios/LAB-Glue).

# Certificados

Nessa Sprint não teve nenhum certificado além do da Udemy

# Desafio

O desafio dessa Sprint foi a realização da segunda etapa do desafio final, que tinha como objetivo utilizar AWS Lambda para realizar a ingestão de dados das APIs da TMDB, e armazenar os dados coletados em um bucket no Amazon S3. 

[Desafio](./desafio/README.md)