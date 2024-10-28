# 1. Escolha e análise dos dados

Para realizar a análise, escolhi a base de dados da Polícia Federal, especificamente o Sistema de Informações de Investigação referente ao mês de junho de 2022. Essa base inclui informações como o tipo de crime, número de operações realizadas, valores e bens apreendidos, quantidade de presos, mandados de busca e apreensão, e tipo de prisão.

Para atender aos requisitos do desafio, filtrei os dados para selecionar registros que apresentassem prisões preventivas ou mandados de busca e apreensão, e que não tivessem ocorrido em território indígena. Com esse filtro, examinei ainda se alguma dessas operações incluía prisões em flagrante.

A partir daí, organizei o DataFrame agrupando as informações por área de crime, buscando identificar qual tipo de crime teve maior ocorrência no período. Fiz também a soma dos valores apreendidos para cada área de crime, além de indicar a presença ou ausência de prisões em flagrante. Por fim, calculei a média de dias que levou para cada crime ser deflagrado desde a data de início, obtendo uma visão mais detalhada sobre o tempo de resposta das operações.

As evidencias do desafio podem ser observadas na pasta [Evidencias](/Sprint_5/evidencias)

# 2. Criação do bucket

Para interagir com os serviços da AWS, instalei a biblioteca `boto3`, que permite realizar operações com a AWS através de scripts, e a `awscli`, ferramenta que possibilita a interação direta com os serviços AWS pelo terminal sem necessidade de acessar o console pelo navegador.

![Instalação da AWS CLI](/Sprint_5/evidencias/install-awscli.png)

Após a instalação, configurei as credenciais da AWS para estabelecer a conexão entre o ambiente local e a nuvem.

![Configuração das Credenciais](/Sprint_5/evidencias/aws-configure.png)

Em seguida, desenvolvi um script em Python (`desafio.py`) para criar o bucket e fazer o upload do arquivo CSV para ele. O código completo pode ser acessado [aqui](/Sprint_5/desafio/desafio.py).

![Screenshot do Bucket](/Sprint_5/evidencias/bucket-01.png)

Importei as bibliotecas `boto3`, além de `NoCredentialsError` e `ClientError` de `botocore` para tratamento de exceções. Defini o nome do bucket (`bucket_name`), o caminho local do arquivo CSV (`csv_file`), e o nome do arquivo no S3 (`s3_file_name`). O cliente S3 foi criado com `boto3.client('s3')`, que permite interagir com o serviço S3.

![Função de Criação do Bucket](/Sprint_5/evidencias/bucket-02.png)

- Função para criar o bucket: `s3.create_bucket(Bucket=bucket_name)` tenta criar o bucket; em caso de sucesso, uma mensagem é exibida. Se ocorrer algum erro, como nome de bucket inválido ou duplicado, o `ClientError` é acionado.

- Função para upload do arquivo: `s3.upload_file(file_name, bucket, s3_file_name)`, que copia o arquivo local para o bucket S3 com o nome especificado. Possíveis erros incluem:
  - `FileNotFoundError`: se o arquivo local não for encontrado.
  - `NoCredentialsError`: se as credenciais da AWS não estiverem disponíveis.
  - `ClientError`: para outros erros, como permissões insuficientes.

Rodei o código e foi possível ver que foi criado com sucesso o Bucket e foi feito o upload do arquivo.  
![Funcionamento do código](/Sprint_5/evidencias/arquivo.png)
![Bucket criado](/Sprint_5/evidencias/bucket.png)

# 3. Criação do DataFrame

A segunda parte do desafio pedia a criação de um script que, a partir de um arquivo armazenado no S3, construísse um DataFrame utilizando a biblioteca **pandas**. O script deveria atender aos seguintes critérios: filtragem usando dois operadores lógicos, duas funções de agregação, uma função condicional, uma de conversão, uma de manipulação de datas e uma de manipulação de strings.

A seguir, apresento o passo a passo para alcançar os resultados desejados. O código completo pode ser encontrado [aqui](/Sprint_5/desafio/analise.py).

#### 3.1 Importação das Bibliotecas e Função para Ler o CSV

![Evidência da Análise](/Sprint_5/evidencias/analise-01.png)

Comecei importando as bibliotecas que seriam utilizadas no script:

- **`boto3`**: biblioteca para interagir com serviços da AWS, como o S3.
- **`pandas`**: biblioteca para manipulação e análise de dados.
- **`numpy`**: biblioteca para cálculos numéricos.
- **`StringIO`**: permite tratar a string lida como um objeto de arquivo, facilitando a leitura de dados pelo **pandas**.

Em seguida, criei uma função para ler o arquivo diretamente do S3:

- **Criação do cliente S3**: Utilizei `boto3.client('s3')` para criar o cliente S3.
- **Obtendo o arquivo CSV**: A função usa `get_object` para obter o arquivo CSV do S3, especificando `Bucket=bucket_name` e `Key=s3_file_name`.
- **Leitura e decodificação**: O conteúdo do arquivo é lido com `.read()` e, em seguida, decodificado para `ISO-8859-1` para evitar problemas de encoding.

#### 3.2 Função para Processar os Dados

![Processar Dados](/Sprint_5/evidencias/analise-02.png)

Após isso, criei a função para processar os dados:

- **Carregamento do CSV**: O CSV é carregado em um DataFrame do **pandas** utilizando `StringIO`, especificando que os dados estão separados por `;` e que o encoding é `ISO-8859-1`.

- **Filtragem dos dados**: Para filtrar os dados, a função aplica uma condição que verifica se `Qtd Prisao Preventiva` ou `Qtd Mandado de Busca e Apreesao` são maiores que zero, excluindo operações que ocorreram em território indígena com a condição `(~df['Atuacao em Territorio Indigena'].str.contains('Sim'))`.

- **Verificação de prisão em flagrante**: Após a filtragem, uma nova coluna chamada `Ha_Prisao_Flagrante` é adicionada ao DataFrame. Esta coluna indica "Sim" se `Qtd Prisao em Flagrante` for maior que zero e "Não" caso contrário.

- **Diferença entre a Data de Início e a Data de Deflagração**: Para calcular a diferença entre as datas, a função realiza os seguintes passos:

   - **Conversão de formato de data**: As colunas `Data do Inicio` e `Data da Deflagracao` são convertidas para o formato datetime utilizando `pd.to_datetime()`, assumindo que o dia é o primeiro. Isso é feito com o argumento `dayfirst=True`, que garante que as datas sejam interpretadas corretamente.
  
   - **Cálculo da diferença em dias**: A diferença em dias é calculada subtraindo `Data do Inicio` de `Data da Deflagracao`. O resultado é armazenado em uma nova coluna chamada `Diferenca_Dias`, representando a quantidade de dias entre os dois eventos.

![Resultados do Processamento](/Sprint_5/evidencias/analise-03.png)

- **Agrupamento dos dados**: Após calcular a diferença entre as datas, realizei o agrupamento dos dados para uma melhor visualização no DataFrame. A função agrupa os dados pela coluna `Area` e calcula as seguintes métricas:

   - **Quantidade de Operações**: Utiliza a função `'size'` para contar quantas operações estão presentes em cada área.
  
   - **Total de Valores Apreendidos**: Para calcular o total de valores apreendidos, a função remove o prefixo `R$`, ajusta os números trocando a vírgula por ponto para que possam ser convertidos em tipo flutuante. Em seguida, soma todos os valores para cada área.
  
   - **Presença de Prisão em Flagrante**: Verifica se houve ao menos um caso de prisão em flagrante na área. A coluna `Ha_Prisao_Flagrante` será marcada como "Sim" se houver pelo menos uma ocorrência, caso contrário, será marcada como "Não".
  
   - **Média da Diferença de Dias**: Calcula a média da coluna `Diferenca_Dias` para determinar a diferença média entre as datas de início e deflagração para cada área.

Esse agrupamento fornece uma visão mais clara sobre a atividade policial em cada área, permitindo identificar padrões e tendências nos dados.

 **Resultado Final**

O `resultado_final` é um dicionário que contém as seguintes informações:

- **Quantidade de Operações por Área**: Um DataFrame que lista a quantidade total de operações realizadas em cada área, facilitando a análise da atividade policial.

- **Quantidade Total de Dinheiro Apreendido**: O total de valores apreendidos, que representa a soma de todos os valores encontrados nas operações filtradas. Essa métrica fornece uma visão clara do impacto financeiro das operações.

- **Flagrante em Cada Área**: Informações sobre a ocorrência de prisões em flagrante em cada área, indicando se houve ou não prisões em flagrante. Essa coluna permite identificar as áreas com maior atividade policial em termos de prisões.

Esse dicionário resume os resultados do processamento dos dados, permitindo uma análise mais profunda das operações e seus resultados.

#### 3.3 Função para Salvar o Resultado em um Arquivo CSV

Após o processamento e o agrupamento dos dados, foi desenvolvida uma função para salvar os resultados em um arquivo CSV local. A função `salvar_resultado_csv` recebe o dicionário `resultado` e um `caminho_arquivo`, que define onde o arquivo CSV será salvo. A imagem abaixo ilustra a execução dessa etapa:

![Evidência da Análise](/Sprint_5/evidencias/analise-04.png)

- **Função de Salvamento em CSV**: A função `salvar_resultado_csv` extrai o DataFrame `Quantidade de Operacoes por Area` de `resultado` e salva-o como CSV. Os parâmetros `sep=';'` e `encoding='ISO-8859-1'` garantem a correta formatação dos dados, especialmente ao lidar com caracteres especiais. A função imprime uma confirmação ao final.

- **Função para Fazer Upload do Arquivo para o S3**: Após o salvamento local do arquivo CSV, criei uma função para realizar o upload para o bucket S3. A função `upload_csv_para_s3` recebe o `bucket_name`, o `caminho_arquivo` local e o `s3_file_name` que será o nome do arquivo no bucket S3.

   - **Criação do Cliente S3**: Utilizamos `boto3.client('s3')` para criar o cliente S3.
   - **Upload para o Bucket**: O método `upload_file` faz o upload do arquivo CSV local para o bucket S3, com o nome especificado.
   - **Confirmação do Upload**: Após o upload, a função exibe uma mensagem confirmando o nome do arquivo e o bucket de destino.

##### Execução do Script Completo

Para executar o processamento completo, definimos os parâmetros e chamamos as funções na seguinte sequência:

1. **Definição do Bucket e do Arquivo**: Define-se o bucket S3 (`bucket_name`) e o nome do arquivo CSV (`s3_file_name`) a ser lido.
2. **Leitura e Processamento do CSV**: A função `ler_csv_do_s3` lê o conteúdo CSV do S3, e `processar_dados` processa os dados.
3. **Salvamento do Resultado em CSV Local**: A função `salvar_resultado_csv` salva o resultado final em um arquivo CSV local (`caminho_arquivo_local`).
4. **Upload do Arquivo para o S3**: A função `upload_csv_para_s3` envia o arquivo CSV local para o bucket S3.

#### Verificação dos Critérios

- **Operadores Lógicos**: Utilizei dois operadores lógicos na filtragem de dados:
  - `|` (OU) para verificar se "Qtd Prisao Preventiva" ou "Qtd Mandado de Busca e Apreesao" são maiores que 0.
  - `&` (E) para excluir registros com "Atuacao em Territorio Indigena" contendo "Sim".

- **Funções de Agregação**:
  - `size` para contar a quantidade de operações por área.
  - `sum()` para somar os valores apreendidos, após a conversão em float.

- **Função Condicional**: Utilizei `np.where` para criar a coluna `Ha_Prisao_Flagrante`, que indica "Sim" ou "Não" dependendo da condição se `Qtd Prisao em Flagrante` é maior que 0.

- **Função de Conversão**: Convertemos valores monetários em texto para float, removendo o símbolo "R$" e ajustando a formatação de milhar e ponto.

- **Manipulação de Datas**: Converti as colunas "Data do Inicio" e "Data da Deflagracao" para o tipo datetime e calculei a diferença em dias entre essas colunas.

- **Manipulação de Strings**: Removi o símbolo de moeda "R$" e converti vírgulas em pontos, para permitir a interpretação correta dos valores como numéricos.

# Resultado Final

![Visualização do Resultado](/Sprint_5/evidencias/resultado-csv.png)

Como resultado final, obtive um arquivo `.csv` com as informações processadas. O arquivo completo pode ser acessado [aqui](/resultado_final.csv).
