# Sprint 5

Nesta Sprint, exploramos os fundamentos da Computação em Nuvem utilizando a **Amazon Web Services (AWS)** como nosso ambiente de trabalho e começamos a nos preparar para a certificação **AWS Certified Cloud Practitioner (CLF-C02)**.

## Cloud Quest: Aprendizado Gamificado

Durante a jornada, tivemos a oportunidade de jogar o **Cloud Quest**, um jogo educacional da AWS que ensina os conceitos de nuvem de forma interativa. Assumimos o papel de exploradores em um mundo virtual, resolvendo desafios práticos relacionados ao armazenamento, redes e segurança, aplicando conceitos da AWS em cenários do mundo real. 

### Ferramentas Aprendidas

Algumas das principais ferramentas que exploramos no Cloud Quest e que solidificaram nosso entendimento foram:

- **Amazon S3 (Simple Storage Service)**: Serviço de armazenamento de objetos escalável e seguro, ideal para hospedar sites estáticos e armazenar dados com alta durabilidade.
  
- **Amazon EC2 (Elastic Compute Cloud)**: Serviço de computação escalável na nuvem que nos permite gerenciar servidores virtuais e ajustar recursos conforme a demanda.

- **Amazon EBS (Elastic Block Store)**: Armazenamento em bloco que fornece volumes persistentes para instâncias EC2, garantindo alta disponibilidade e durabilidade para dados críticos.

- **Amazon VPC (Virtual Private Cloud)**: Ferramenta para criar redes virtuais isoladas, oferecendo controle completo sobre a topologia da rede e políticas de segurança.

- **Amazon RDS (Relational Database Service)**: Serviço gerenciado que facilita a configuração e operação de bancos de dados relacionais com backups automáticos e escalabilidade.

- **Amazon DynamoDB**: Banco de dados NoSQL gerenciado, com baixa latência e escalabilidade automática, ideal para aplicações que exigem desempenho rápido e consistente.

- **Amazon EFS (Elastic File System)**: Sistema de arquivos elástico e escalável, projetado para ser acessado simultaneamente por várias instâncias EC2.

- **IAM (Identity and Access Management)**: Ferramenta essencial para gerenciar identidades e permissões de usuários na AWS, garantindo segurança e conformidade.

- **Amazon EC2 Auto Scaling**: Ferramenta que ajusta automaticamente a quantidade de instâncias EC2 com base na demanda, otimizando custos e garantindo alta disponibilidade.

## Certificação AWS Certified Cloud Practitioner (CLF-C02)

Ao longo da Sprint, também finalizamos o curso de preparação para o exame **AWS Certified Cloud Practitioner (CLF-C02)**. Este curso me proporcionou uma visão completa dos principais conceitos de computação em nuvem, ajudando a consolidar minha compreensão sobre:

### Fundamentos da Computação em Nuvem

Entendi como conceitos como **elasticidade**, **escalabilidade** e os diferentes **modelos de serviço (IaaS, PaaS, SaaS)** formam a base da computação em nuvem. Também explorei como a AWS se destaca como um dos maiores provedores de nuvem no mundo, oferecendo uma infraestrutura global robusta e segura.

### Segurança na Nuvem

Outro ponto central do curso foi a **segurança na AWS**, onde aprendi sobre o **Modelo de Responsabilidade Compartilhada**. Este modelo explica que a AWS é responsável pela segurança da nuvem, enquanto os usuários são responsáveis pela segurança dentro dela. O **AWS IAM** também se destacou como uma ferramenta essencial para gerenciar o controle de acesso e permissões.

### Modelos de Preços e Suporte

Também foi importante entender os **modelos de preços da AWS**, que seguem a lógica de pagar apenas pelo que se usa (**pay-as-you-go**). Utilizei o **AWS Pricing Calculator** para estimar custos e aprendi práticas recomendadas para otimizar despesas, mantendo a eficiência.

### Arquitetura e Alta Disponibilidade

Por fim, explorei princípios de **arquitetura em nuvem**, aprendendo a criar sistemas resilientes e com alta disponibilidade. A AWS facilita isso com suas **zonas de disponibilidade** e **regiões**, que garantem que as aplicações continuem funcionando, mesmo diante de falhas de infraestrutura.

# Exercicíos
No exercício proposto, realizei um laboratório para explorar as capacidades do serviço AWS S3, onde segui um passo a passo para configurar um bucket para hospedagem de site estático. Durante o laboratório, criei um bucket e habilitei a opção de hospedagem de conteúdo estático, configurando o documento de índice (index.html) e o documento de erro (404.html). Em seguida, ajustei as permissões de acesso público por meio de uma política de bucket que permite acesso de leitura, o que tornou o conteúdo acessível publicamente. Para concluir, testei o endpoint do bucket, verificando que o site estava funcionando corretamente, com redirecionamento de erros personalizados e download de arquivos, completando a configuração da hospedagem estática no S3.
As evidencias sobre o exercicíos pode ser visto na pasta [Exercicíos](./exercicios)

# Certificados

![Certificado AWS](/Sprint_5/certificados/certificado.png)

A badge da conclusão do game Cloud Quest, pode ser vista no link:

https://www.credly.com/badges/8b704b3a-0f1c-44b8-95a3-da425c9e0563/public_url

# Desafio

Neste desafio, apliquei conhecimentos práticos de AWS manipulando arquivos no S3. Comecei acessando o portal de dados do governo para selecionar um arquivo para análise e, em seguida, criei um script em Python usando boto3 para configurar um bucket. Após isso, desenvolvi um segundo script para ler um arquivo CSV diretamente do bucket S3, processar seus dados e, finalmente, salvar os resultados em um novo arquivo CSV, que também foi enviado de volta para o S3.

[Desafio](./desafio/README.md)
