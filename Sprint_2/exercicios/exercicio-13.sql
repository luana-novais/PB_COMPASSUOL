SELECT 
	cdpro,
	nmcanalvendas,
	nmpro,
 	SUM(qtd) as quantidade_vendas
from tbvendas  
where status = 'Concluído'
group by nmcanalvendas,cdpro,nmpro 
ORDER by quantidade_vendas
limit 10