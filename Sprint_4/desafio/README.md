## Etapa 1 
Foi pedido para criar uma imagem através de um arquivo de instruções dockerfile que executasse o ``carguru.py``, para criar o dockerfile utilizei os seguintes comandos: 

![alt text](/Sprint_4/evidencias/dockerfile.png)

``FROM`` - especifica a imagem base que será usada para criar a nova imagem Docker e define o ambiente em que o restante do Dockerfile será executado. No caso do desafio este comando diz ao Docker para usar a imagem oficial do Python na versão 3.9

``WORDKIR`` - define o diretório de trabalho para as instruções subsequentes no Dockerfile. Todas as operações que ocorrem após a instrução WORKDIR serão realizadas nesse diretório.

``COPY`` - utilizado para copiar arquivos e diretórios do sistema de arquivos do host para o sistema de arquivos da imagem Docker durante o processo de construção da imagem.

``CDM`` - especifica o comando que será executado quando um container for iniciado a partir da imagem, no caso do desafio este comando diz ao Docker para executar o script ``carguru.py`` usando o interpretador Python quando o container for iniciado.

###### Como Construir a Imagem Docker
Para construir a imagem Docker do projeto, usei o comando ``docker buil`` no terminal, no diretório onde o Dockerfile e carguru.py estão localizados. Na imagem a baixo podemos ver que a imagem foi criada com sucesso.

![alt text](/Sprint_4/evidencias/image.png)

##### Como Executar o Container
Depois de construir a imagem, executei o container com o seguinte comando ``docker run`` 

![alt text](/Sprint_4/evidencias/execução.png)

## Etapa 2
É possível reutilizar conteiners? 
Sim, é possível reutilizar containers no Docker. Para reutilizar um container parado, você pode iniciá-lo novamente usando o comando docker start.
1. Listar todos os containers (incluindo os parados):
Utiliza o comando ``docker ps -a`` para listar todos os containers, incluindo os que estão parados.

![alt text](/Sprint_4/evidencias/comando-ps.png)

2. Iniciar container parado:
Para reutilizar (ou reiniciar) um container parado, usei o comando ``docker start`` e depois dei um ``docker ps`` novamente para ver que o container estava aberto.

![alt text](/Sprint_4/evidencias/comando-start.png)

## Etapa 3

##### Criar o script
Para a etapa 3, foi solicitado criar um container que permitisse receber input durante a sua execução. Primeiro criei o script em Python para receber os inputs.
[Script da etapa 3](/Sprint_4/desafio/etapa-3/etapa-3.py)

![alt text](/Sprint_4/evidencias/etapa-3/script.png)

Explicação do código:
- Importação do módulo hashlib: O hashlib é a biblioteca padrão do Python que implementa algoritmos de hash, incluindo SHA-1.
- ``while true`` - para criar um loop infinito, mantendo o container ativo e aguardando inputs do usuário. 
- ``hashlib.sha1()`` - cria um objeto de hash SHA-1, que será usado para calcular o hash da string fornecida.
- ``string.encode()`` - transforma a string em bytes, pois as funções de hash esperam um input no formato de bytes, e não de string. O método .encode() converte a string em uma sequência de bytes utilizando a codificação padrão UTF-8.
- ``.hexdigest()`` converte o hash gerado em uma string hexadecimal, que é a forma comum de representação de hashes.


Fluxo do Programa:
O programa solicita ao usuário que digite uma string.
A string é convertida em bytes e o hash SHA-1 é calculado.
O valor do hash é convertido em uma string hexadecimal.
O programa exibe o hash correspondente à string digitada.
O loop recomeça, permitindo que o usuário digite outra string para calcular um novo hash.

##### Criar a imagem
Depois de criar o script, fiz o Dockerfile, informando ao Docker como construir a imagem do container

![alt text](/Sprint_4/evidencias/etapa-3/imagem-3.png)


No terminal, naveguei até o diretório onde estava o Dockerfile e o etapa-3.py, e executei o seguinte comando para construir a imagem Docker:

![alt text](/Sprint_4/evidencias/etapa-3/image.png)

Com a imagem criada, rodei o container em modo interativo usando o comando ``docker run -it`` e armazenei alguns dados para testar o funcionamento do script. 

![alt text](/Sprint_4/evidencias/etapa-3/comando-run.png)