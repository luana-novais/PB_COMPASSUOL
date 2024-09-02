#!/bin/bash

# Caminho onde os relatórios estão armazenados
CAMINHO_RELATORIOS="/home/luana/PB_LUANA_NOVAIS/Sprint_1/desafio/ecommerce/vendas/backup"

# Nome do arquivo final consolidado
ARQUIVO_FINAL="$CAMINHO_RELATORIOS/relatorio_final.txt"

# Consolida todos os relatórios em um único arquivo
cat "$CAMINHO_RELATORIOS"/relatorio-*.txt > "$ARQUIVO_FINAL"

