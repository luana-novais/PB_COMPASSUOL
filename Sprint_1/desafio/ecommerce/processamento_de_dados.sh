#!/bin/bash
#criei a pasta vendas
mkdir -p vendas

#copiei o arquivo de vendas
cp dados_de_vendas.csv vendas/

#subdiretorio backup
mkdir -p vendas/backup

#capturando a data atual e armazenando em uma variavel DATA
DATA=$(date +%Y%m%d)

#copiando o arquivo de vendas com a data atual 
cp vendas/dados_de_vendas.csv vendas/backup/dados-$DATA.csv

#movendo o arquivo e renomeando 
mv vendas/backup/dados-$DATA.csv vendas/backup/backup-dados-$DATA.csv
 

