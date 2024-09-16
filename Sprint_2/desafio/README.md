# Etapas

#### Normalização da base de dados

Para otimizar o banco de dados e deixar com uma forma mais organizada, realizei a normalização da tabela original utilizando o DBeaver, a tabela tinha informações sobre clientes, carros, combustíveis, vendedores e locações. O processo de normalização consistiu em dividir essa tabela em várias tabelas menores, eliminando a redundância e organizando os dados de forma lógica. A tabela original pode ser obaervada na imagem abaixo:

<p align="center">
  <img src='/Sprint_2/evidencias/concessionaria-original.png' alt="Tabela original" width="200px" />
</p>


1. Análise da Tabela Original
A primeira etapa foi analisar os dados da tabela tb_locacao. Identifiquei que a tabela armazenava informações relacionadas a várias entidades (clientes, carros, combustíveis, vendedores e locações) em uma única estrutura, o que gerava redundância e dificultava a manutenção dos dados. Por exemplo, o nome de um cliente aparecia repetidas vezes para cada nova locação. 
A tb_locação já estavá na 1ª Forma Normal (1NF), não havia conjuntos de valores repetidos ou múltiplos valores em uma mesma coluna. Precisei fazer a 2FN para eliminar dependencias parciais, criando tabelas para organização dos dados.

2. Criação das Tabelas Normalizadas
Para organizar melhor os dados, criei cinco tabelas: Clientes, Carro, Combustivel, Vendedor e Locacao. Cada uma dessas tabelas armazena dados de uma entidade específica, com chaves primárias únicas para cada registro.
Para a criação das tabelas utilizei o comando ``CREATE TABLE``, cada tabela tem um conjunto de colunas, e para cada coluna, você define o tipo de dado que ela armazenará. E o comando ``FOREIGN KEY`` para conectar as tabelas entre si através das chaves estrangeiras, garantindo a integridade referencial.
  
3. Inserção dos Dados nas Tabelas Normalizadas
Com as tabelas criadas, o próximo passo foi inserir os dados da tabela original (tb_locacao) nas tabelas recém-criadas. Para evitar a duplicidade, utilizei o comando ``INSERT OR IGNORE``, garantindo que apenas os registros únicos fossem inseridos.

4. Remoção da Tabela Original
Depois de transferir os dados para as novas tabelas, removi a tabela original tb_locacao para evitar redundância e liberar espaço no banco de dados. Utilizei o comando: ``DROP TABLE IF EXISTS tb_locacao``

O script completo de todos os comandos utilizados para criação das tabelas pode ser observado abaixo:  
![](/Sprint_2/evidencias/normalizacao.sql)
### Modelo Relacional
#### Desenho do Modelo Relacional:
Após a normalização dos dados, o modelo relacional ficou da seguinte forma

<p align="center">
  <img src='/Sprint_2/evidencias/modelo-relacional.png' alt="Modelo relacional"/>
</p>


#### Descrição dos Relacionamentos:

- A tabela `Clientes` está relacionada com `Locacao` através da chave estrangeira `idCliente`.
- A tabela `Carro` está relacionada com `Locacao` através da chave estrangeira `idCarro`.
- A tabela `Vendedor` está relacionada com `Locacao` através da chave estrangeira `idVendedor`.
- A tabela `Carro` está relacionada com `Combustivel` através da chave estrangeira `idCombustivel`.


### Modelo Dimensional

Depois, converti o modelo para o modelo dimensional, simplificando a estrutura em uma tabela fato, contendo métricas quantitativas, e tabelas dimensão, que descrevem os dados. Isso facilita consultas analíticas e relatórios, com foco em performance e agregação de dados.
Para criar o modelo pensei na seguinte questão ``Qual a receita total gerada pelas locações? Como essa receita está distribuída entre carros, clientes e vendedores?``

Para responder essas questões, criei 4 tabelas(views) dimensões:
- ``dim_cliente`` (nomeCliente, cidadeCliente, estadoCliente)
- ``dim_carro`` (marcaCarro, modeloCarro, classiCarro, anoCarro)
- ``dim_vendedor`` (nomeVendedor, sexoVendedor, estadoVendedor)
- ``Data`` (mês, ano, dia da semana, etc.)

E criei a tabela fato_locacao que armazena os fatos relacionados às locações, como a receita total gerada. Essa tabela permite que os dados sejam analisados por cliente, carro, vendedor ou período. As principais métricas são qtdDiaria, que representa a quantidade de diárias alugadas, e vlrDiaria, que é o valor diário da locação. Com base nisso, criei a nova métrica receitaTotal, calculada como qtdDiaria * vlrDiaria, que representa a receita gerada por cada locação."
A tabela possui chaves estrangeiras que conectam com as dimensões de cliente, carro, vendedor e tempo:

- ``idLocacao`` - identifica cada locação.
- ``idCliente`` - relaciona-se à dimensão cliente.
- ``idCarro`` `- relaciona-se à dimensão carro.
- ``idVendedor`` - relaciona-se à dimensão vendedor.
- ``dataLocacao`` - liga-se à dimensão de tempo.

O script para a criação das tabelas pode ser observado abaixo: 
![](/Sprint_2/evidencias/modelo-dimensional.sql)
O desenho do modelo dimensional ficou da seguinte maneira: 
<p align="center">
  <img src='/Sprint_2/evidencias/modelo-dimensional.png' alt="modelo dimensional"/>
</p>
Para testar se estava funcionando tudo corretamente, fiz o script seguinte para responder as perguntas propostas:

![](/Sprint_2/evidencias/perguntas-dimensional.sql)