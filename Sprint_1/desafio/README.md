
# Etapas


##### 1. ORIENTAÇÕES

- A primeira parte do desafio padia para criar um repositório privado no GitHub e adicionar o colaborador da Compass UOL. Em seguida, escolhi o editor de texto que utilizaria para resolver o desafio. Optei pelo Visual Studio Code (VS Code) e decidi usar o Windows Subsystem for Linux (WSL) em vez de uma máquina virtual.
- Após seguir as orientações iniciais, criei os diretórios e arquivos necessários utilizando comandos básicos do Linux que aprendi durante o curso. Para criar os diretórios, utilizei o comando mkdir. Durante a criação do arquivo Markdown, tentei usar o comando cat, que pode ser usado para criar, unir ou exibir arquivos. No entanto, cometi um erro de sintaxe, resultando em uma falha como pode ser visto na imagem. Em vez disso, usei o comando touch, que permite tanto criar arquivos vazios quanto controlar as modificações realizadas nos arquivos.

![Comandos utilizados para criação das pastas no sistema operacional Linux](/Sprint_1/evidencias/3-pastas.png)

- Com os diretórios configurados, executei os comandos do Git para subir o projeto para o repositório no GitHub. Primeiro, utilizei o comando git init para inicializar o repositório local e criar os arquivos necessários para o sistema Git. Em seguida, usei o comando git add para adicionar os arquivos ao controle de versão. O próximo passo foi realizar o commit das mudanças, utilizando o comando git commit para registrar as alterações feitas no repositório local. Como pode ser visto na imagem, ocorreu um erro nessa etapa, pois eu não havia configurado corretamente o nome e o e-mail no Git. 

![Comandos utilizados para criação do repo remoto](/Sprint_1/evidencias/4-commit.png)
 

- Após corrigir essas configurações, criei um branch do projeto, definindo-o como a ramificação principal (master), onde todas as ramificações adicionais seriam salvas, caso houvesse mais de um branch. Depois, utilizei o comando git remote add para associar o repositório local ao repositório remoto no GitHub. E por ultimo executei o comando git push para enviar o código para o repositório remoto.

![Comandos utilizados para envio do repo local](/Sprint_1/evidencias/5-branch.png)
 
- Durante a realização do desafio, precisei renomear o arquivo Markdown de 'apresentação' para 'README', conforme solicitado nas instruções. Também alterei o nome do diretório de 'COMPASS-UOL' para 'PB_LUANA_NOVAIS', para facilitar a identificação do projeto e deixando claro a quem o repositório se refere.


##### 2. PREPARAÇÃO

- Para iniciar a resolução do desafio, usei o comando **mkdir** para criar o repositorio ecommerce e dentro dele colocar o arquivo *dados_de_vendas.csv*. 

![comandos utilizados para criar repo ecommerce](/Sprint_1/evidencias/6-ecommerce.png)

- O arquivo dados_de_vendas.csv foi baixando dentro de uma pasta no windows, e para que conseguisse copiar ela para dentro do sistema Linux usei o comando **cp /mnt** para mover o arquivo para o diretorio ecommerce. 

![comando usado para copiar o arquivo](/Sprint_1/evidencias/7-copia-dados.png)

##### 3. CRIANDO UM ARQUIVO EXECUTÁVEL
- Na imagem abaixo, estão os comandos utilizados para a criação do script:

![como criei o script](/Sprint_1/evidencias/8-script.png)

- **Criar o diretório vendas:** Usei o comando **mkdir -p**, onde a opção *-p* previne erros caso o diretório já exista.
- **Cópia do arquivo dados_de_vendas:** Utilizei o comando **cp** para copiar o arquivo da pasta ecommerce para a pasta vendas.
- **Criar o subdiretório backup:** Com o comando **mkdir**, criei um subdiretório dentro da pasta vendas, destinado a armazenar os backups das vendas.
- **Variável DATA:** Criei uma variável chamada DATA que armazena a data atual, utilizando o comando **date** no formato +%Y%m%d. Isso gera a data no formato `aaaa/mm/dd`, que será usado para nomear os arquivos.
- **Cópia do arquivo para a pasta backup:** Usei o comando **cp** para copiar o arquivo e, no caminho de destino, utilizei a variável `$DATA` para que o arquivo já fosse nomeado com a data em que o script foi executado.
- **Renomeando o arquivo:** Como solicitado, alterei o nome do arquivo para `backup_dados_$DATA` usando o comando *mv*.

##### 3.1 Criando o Relatório


Para criar o relatório, primeiro defini algumas variáveis:

- **Data do sistema operacional com hora:** Utilizei o comando **date** para obter a data e a hora atuais do sistema.
- **Primeira data de venda:** Com o comando **tail -n +2**, exibi todas as linhas do arquivo, ignorando a primeira linha do cabeçalho. Em seguida, usei **head -n 1** para selecionar a primeira linha, que corresponde ao primeiro registro de venda. O comando **cut -d ',' -f 5** foi utilizado para extrair a quinta coluna, que contém a data.
- **Última data de venda:** Utilizei **tail -n 1** para exibir a última linha do arquivo e **cut** para extrair a quinta coluna.
- **Quantidade de itens diferentes vendidos:** Usei o comando **cut -d',' -f2** para extrair a segunda coluna, que contém os nomes dos produtos. Com o comando **sort**, ordenei os nomes em ordem alfabética e, em seguida, usei **uniq** para remover os duplicados. Por fim, **wc -** contou o número de linhas resultantes, representando os produtos diferentes vendidos.
- **Criação do relatório:** Utilize o comando **echo** para escrever o conteúdo das variáveis definidas anteriormente em um arquivo `.txt`. Usei o operador `>` para definir a primeira linha do relatório e o comando `>>` para adicionar as próximas linhas sem sobrescrever as anteriores.
- **Adição das 10 primeiras linhas:** Utilizei **head** com a opção **-n 10** para adicionar as primeiras 10 linhas do arquivo ao relatório.
- **Compressão dos arquivos:** Usei o comando **cd** para acessar o diretório **backup**, seguido do comando **zip** para comprimir os arquivos.
- **Remoção dos arquivos originais:** Por fim, utilizei o comando **rm** para remover os arquivos originais e as cópias que não foram comprimidas.
    
##### 4. Agendar a execução do processamento
- Para realizar o agendamento, primeiro verifiquei se o arquivo estava com a permissão de executar o script. Com o comando **chmod**  para deixer o arquivo executavél. 
- Depois com o comando **crontab -e** defini para que o script rodasse de quarta(3) até sabado(6). Especifiquei o caminho absoluto do script *processamento_de_dados.sh* e depois usei **>>** para redirecionar a saída do script para o arquivo processamento_de_dados.log. Junto com **2>&1** que redireciona a saída de erro para o arquivo processamento_de_dados.log. Isso garante que tanto as mensagens normais quanto as mensagens de erro sejam registradas no mesmo arquivo de log.

![como configurei o agendamento](/Sprint_1/evidencias/9-cron.png)

- Tive bastante dificuldade nessa etapa, enfrentando vários erros, como mostrado na imagem, especialmente relacionados ao caminho do diretório. Após muita pesquisa, descobri que o problema estava em uma barra invertida. Finalmente, conseguimos verificar que os agendamentos foram executados conforme o solicitado.

![arquivo log mostrando quando o cron estava errado e quando deu certo](/Sprint_1/evidencias/10-log.png)

##### 5. Novo relatório

- O desafio pedia para criar um novo script para juntar todos os relatorios gerados em um unico chamado relatorio-final.txt. Primeiro defini o caminho onde estava os relatorios, e usei o comando **cat** para juntar todos os arquivos e redirecionar a saída diretamente para o arquivo relatorio_final.txt. Se o arquivo já existir, ele será sobrescrito.

![script consolidador](/Sprint_1/evidencias/consolidador.png)

- Por ultimo utilizei o comando **chmod** para deixar o consolidador executavél, e por fim rodei o script manualmente para gerar o novo relatorio. 

![execução do script](/Sprint_1/evidencias/11-relatorio-final.png)

##### 6. Resultados
Consegui completar o desafio com sucesso, atingindo todos os objetivos. Realizei todas as etapas, desde a manipulação dos dados no CSV até a automação da execução do script com crontab, conforme planejado. O script rodou corretamente e gerou o relatório de vendas dentro do prazo, atendendo às expectativas e requisitos do desafio. Esse processo foi uma ótima oportunidade para aplicar e consolidar meu conhecimento nas ferramentas e conceitos utilizados.

![resultado do desafio](/Sprint_1/evidencias/resultado.png)

**Dia 1**
![dia-1](/Sprint_1/evidencias/dia-1.png)

**Dia 2**
![dia-2](/Sprint_1/evidencias/dia-2.png)

**Dia 3**
![dia-3](/Sprint_1/evidencias/dia-3.png)

**Dia 4**
![dia-4](/Sprint_1/evidencias/dia-4.png)
