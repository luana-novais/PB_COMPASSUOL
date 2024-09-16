SELECT 
estado,
nmpro, 
ROUND(AVG(qtd),4) as quantidade_media 
FROM tbvendas 
WHERE status = 'Concluído'
group by estado,nmpro 
order by estado,nmpro 