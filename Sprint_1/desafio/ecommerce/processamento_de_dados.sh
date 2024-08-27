#!/bin/bash

# Criação do diretório vendas
mkdir -p /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas

# Cópia do arquivo de vendas
cp /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/dados_de_vendas.csv /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/

# Criação do subdiretório backup
mkdir -p /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup

# Captura da data atual
DATA=$(date +%Y%m%d)

# Cópia do arquivo para o diretório de backup com a data atual
# Usando caminho relativo
cp vendas/dados_de_vendas.csv vendas/backup/dados-$DATA.csv

# Renomeação do arquivo no backup
mv /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup/dados-$DATA.csv /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup/backup-dados-$DATA.csv

# Criação do relatório
data_sistema=$(date +"%Y/%m/%d %H:%M")
primeira_data=$(tail -n +2 /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup/backup-dados-$DATA.csv | head -n 1 | cut -d ',' -f 5)
ultima_data=$(tail -n 1 /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup/backup-dados-$DATA.csv | cut -d ',' -f 5)
quantidade_itens=$(cut -d ',' -f 3 /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup/backup-dados-$DATA.csv | sort | uniq | wc -l)

echo "Data do sistema operacional: $data_sistema" > /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup/relatorio.txt
echo "Data do primeiro registro de venda: $primeira_data" >> /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup/relatorio.txt
echo "Data do último registro de venda: $ultima_data" >> /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup/relatorio.txt
echo "Quantidade total de itens diferentes vendidos: $quantidade_itens" >> /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup/relatorio.txt

# Adição das primeiras 10 linhas do CSV ao relatório
head -n 10 /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup/backup-dados-$DATA.csv >> /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup/relatorio.txt

cd /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup

# Compressão do arquivo CSV
zip backup-dados-$DATA.zip backup-dados-$DATA.csv

# Remoção dos arquivos originais
rm /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/backup/backup-dados-$DATA.csv
rm /home/luana/trainee-repo-template/Sprint_1/desafio/ecommerce/vendas/dados_de_vendas.csv
