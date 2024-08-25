#!/bin/bash
# Criando o diretório vendas
mkdir -p vendas

# Copiando o arquivo de vendas
cp dados_de_vendas.csv vendas/

# Criando o subdiretório backup dentro de vendas
mkdir -p vendas/backup

# Capturando a data atual e armazenando em uma variável DATA
DATA=$(date +%Y%m%d)

# Copiando o arquivo de vendas com a data atual
cp vendas/dados_de_vendas.csv vendas/backup/dados-$DATA.csv

# Movendo o arquivo e renomeando
mv vendas/backup/dados-$DATA.csv vendas/backup/backup-dados-$DATA.csv

# Criando o relatório txt
data_sistema=$(date +"%Y/%m/%d %H:%M")
primeira_data=$(head -n 2 vendas/backup/backup-dados-${DATA}.csv | tail -n 1 | cut -d ',' -f 1)
ultima_data=$(tail -n 1 vendas/backup/backup-dados-${DATA}.csv | cut -d ',' -f 1)
quantidade_itens=$(cut -d ',' -f 2 vendas/backup/backup-dados-${DATA}.csv | sort | uniq | wc -l)

# Escrevendo no relatório
echo "Data do sistema operacional: $data_sistema" > vendas/backup/relatorio.txt
echo "Data do primeiro registro de venda: $primeira_data" >> vendas/backup/relatorio.txt
echo "Data do último registro de venda: $ultima_data" >> vendas/backup/relatorio.txt
echo "Quantidade total de itens diferentes vendidos: $quantidade_itens" >> vendas/backup/relatorio.txt

# Mostrando as primeiras 10 linhas do arquivo de backup e adicionando ao relatório
head -n 10 vendas/backup/backup-dados-${DATA}.csv >> vendas/backup/relatorio.txt

# Comprimindo os arquivos e limpando os dados
zip -r "vendas/backup/backup-dados-${DATA}.zip" "vendas/backup/backup-dados-${DATA}.csv"
rm "vendas/backup/backup-dados-${DATA}.csv"
rm vendas/dados_de_vendas.csv
