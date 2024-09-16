SELECT 
	t2.nmvdd as 'vendedor',
	SUM((t.qtd * t.vrunt)) as 'valor_total_vendas',
	ROUND(t2.perccomissao * SUM(t.qtd*t.vrunt)/100, 2) as 'comissao'
FROM tbvendas t 
left join tbvendedor t2 
	on t.cdvdd = t2.cdvdd 
WHERE status = 'Concluído'
group by t2.nmvdd 
order by comissao DESC 