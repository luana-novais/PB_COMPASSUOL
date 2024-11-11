# Curso Noções Básicas de Analytics - Parte 1

**Analytics** é o processo de aplicar técnicas especializadas para extrair valor de dados brutos.  

**Análise de Dados** é a prática de interpretar dados para tomar decisões informadas. Existem quatro tipos principais: descritiva, diagnóstica, preditiva e prescritiva, cada uma com um objetivo específico.

#### Inteligência Artificial (IA) e Machine Learning (ML):
- **IA**: Criação de máquinas que executam tarefas que normalmente requerem inteligência humana.
- **Modelo de ML**: Um programa que aprende a identificar padrões em dados e pode fazer previsões (analytics preditiva) ou sugerir ações (analytics prescritiva).
- **Algoritmo de ML**: Identifica padrões e faz previsões ou recomenda ações.
- **ML na AWS**: A AWS oferece serviços de IA e ML para facilitar a análise de dados, reduzir custos e integrar inteligência em aplicações sem a necessidade de experiência em ML.

### Amazon Q Developer:
- Ferramenta que usa processamento de linguagem natural para gerar código automaticamente, ajudando desenvolvedores com preenchimento e segurança de código.

#### Big Data e os 5 V’s:
- **Volume**: Grandes volumes de dados que precisam de infraestrutura escalável, como Amazon S3 e Amazon Redshift.
- **Variedade**: Diferentes tipos de dados, como dados estruturados e não estruturados, com serviços como Amazon RDS e Amazon DynamoDB.
- **Velocidade**: A necessidade de processar dados rapidamente, com serviços como Amazon Kinesis e AWS Lambda.
- **Veracidade**: Garantir a precisão dos dados, usando ferramentas como AWS Glue e Amazon DataZone.
- **Valor**: Transformar dados em insights valiosos com serviços como Amazon QuickSight e Amazon SageMaker.

#### Tipos de Analytics:
- **Analytics Descritiva**: Usa gráficos e tabelas para descrever dados históricos.
- **Analytics Diagnóstica**: Investiga causas de eventos, com técnicas como mineração de dados e correlações.
- **Analytics Preditiva**: Utiliza machine learning e previsões para prever eventos futuros.
- **Analytics Prescritiva**: Recomendação de ações com técnicas como simulação e redes neurais.

#### Serviços AWS para Analytics:
- **Amazon S3, Redshift e EMR**: Usados para armazenar e processar grandes volumes de dados.
- **AWS Glue, Kinesis e Lambda**: Ajudam no processamento e transformação de dados em tempo real.
- **Amazon QuickSight e Athena**: Usados para visualização e análise de dados interativa, otimizando a tomada de decisões.

Esses conceitos ajudam a construir uma base sólida para o uso de ferramentas de análise de dados e IA.

# Curso Noções Básicas de Analytics - Parte 2

#### Data Lake:
- Repositório centralizado para armazenar dados em qualquer formato, estruturado ou não estruturado, em grande escala. Permite executar diferentes tipos de analytics, como big data e machine learning.

#### Data Warehouse:
- Repositório centralizado projetado para analytics, coletando dados de várias fontes e os organizando para consultas rápidas.

#### Arquitetura de Dados Moderna:
- Combina data lakes, data warehouses e armazenamentos específicos para otimizar o fluxo e análise de dados.
- A **malha de dados** tem três pilares principais: dados como produto, governança central e acesso comum.
- **Amazon DataZone**: Ferramenta que gerencia e compartilha dados dentro dessa malha de dados.

#### Serviços AWS para Arquitetura de Dados Moderna:
- **Amazon S3**: Armazenamento escalável de dados.
- **Amazon Glue**: Acesso unificado aos dados e processo de ETL.
- **AWS Lake Formation**: Governança centralizada para data lakes.
- **Amazon Athena**: Análise interativa de dados no Amazon S3 usando SQL.

#### Serviços AWS para Analytics com Propósito Específico:
- **Amazon Redshift**: Data warehouse na nuvem.
- **Amazon EMR**: Plataforma para big data.
- **Amazon Aurora**: Banco de dados OLTP.
- **Amazon DynamoDB**: Banco de dados NoSQL.
- **Amazon OpenSearch Service**: Pesquisa e analytics de dados não estruturados.
- **Amazon SageMaker**: Plataforma para machine learning.

# Serverless Analytics

No curso "Serverless Analytics" da AWS, aprendi como conectar e processar dados de diversas fontes para tomar decisões baseadas em dados. As ferramentas exploradas foram:
- **AWS IoT Analytics**: Para coletar e analisar dados de dispositivos IoT.
- **Amazon Cognito**: Para gerenciar autenticação e acesso aos aplicativos.
- **AWS Lambda**: Para automatizar processos com funções de código.
- **Amazon SageMaker**: Para criar, treinar e implantar modelos de machine learning.

Essas ferramentas me capacitaram para desenvolver soluções de análise de dados escaláveis e robustas.

# Introduction to Amazon Athena

No curso "Introduction to Amazon Athena", aprendi a usar o Amazon Athena para consultar dados armazenados no Amazon S3. O curso abordou as etapas básicas de implementação, como criar um banco de dados e executar consultas SQL no console da AWS. O Athena é uma ferramenta poderosa para análise de grandes volumes de dados de maneira rápida e eficiente.

# AWS Glue Getting Started

No curso de introdução ao AWS Glue, aprendi que ele é uma ferramenta de integração de dados gerenciada pela AWS, simplificando o processo de ETL. O Glue facilita a criação de pipelines de ETL e a automação de transformações, integrando-se com outros serviços da AWS.

#### AWS Glue Studio e AWS Glue DataBrew:
- **Glue Studio**: Interface visual para catalogar e executar transformações de ETL.
- **AWS Glue DataBrew**: Ferramenta para criar perfis de dados e realizar verificações de qualidade, como a detecção de PII.

O curso também abordou a estrutura de custos do AWS Glue.

# Amazon EMR Getting Started

No curso Amazon EMR Getting Started, aprendi sobre o Amazon EMR, uma plataforma para processamento de grandes volumes de dados. O curso abordou:
- **EMR Serverless**: Para executar trabalhos de Spark de forma escalável, sem gerenciar servidores manualmente.
- **Amazon EMR Studio**: Interface integrada para criar e gerenciar notebooks e recursos do EMR.

# Getting Started with Amazon Redshift

No curso "Getting Started with Amazon Redshift", aprendi como o Redshift funciona como uma solução de data warehouse na nuvem, projetada para análises rápidas e escaláveis de grandes volumes de dados. O curso abordou a criação de clusters, carregamento de dados e realização de consultas.

# Best Practices for Data Warehousing with Amazon Redshift

O curso sobre práticas recomendadas para data warehousing com o Redshift abordou:
- **Design de Tabelas**: Para otimizar a estrutura de dados e melhorar o desempenho das consultas.
- **Técnicas de Ingestão de Dados**: Como carregar dados para o Redshift de maneira eficiente.
- **Dimensionamento de Nós e Clusters**: Impacta diretamente no desempenho e custo do Redshift.

# Amazon QuickSight - Getting Started

No curso "Amazon QuickSight - Getting Started", aprendi como utilizar o QuickSight, uma ferramenta de visualização e análise de dados. O curso cobriu:
- **Criação de Conjuntos de Dados**: Como importar e preparar dados para análise.
- **Criação de Análises Visuais**: Usando gráficos e tabelas.
- **Publicação de Painéis**: Para compartilhar insights com outras pessoas.
- **QuickSight Q**: Permite fazer perguntas em linguagem natural sobre os dados.

# Exercicíos

Nessa Sprint fizemos alguns laboratorios para treinar o uso da AWS, a resolução dos exercicíos pode ser visto abaixo: 

##### LAB S3
[Resultados](../Sprint_6/exercicios/LAB-S3)

##### LAB Athena
[Resultados](../Sprint_6/exercicios/LAB-Athena)

##### LAB Lambda
[Resultados](../Sprint_6/exercicios/LAB-Lambda)

# Certificados

Durante a Sprint fizemos 9 cursos da plataforma AWS, os certificados se enconta na pasta [certificados.](./Sprint_6/certificados)

# Desafio

Nesta sprint, iniciamos a preparação para o desafio final, que será a construção de um Data Lake para filmes e séries, incluindo as etapas de ingestão, armazenamento, processamento e consumo dos dados. O desafio será dividido em cinco entregas, e nesta etapa realizamos a primeira entrega.

[Desafio](./desafio/README.md)





