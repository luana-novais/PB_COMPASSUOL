select 
	cddep, 
    nmdep, 
    dtnasc,
    sum(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas
from tbdependente
join tbvendedor 
    on tbdependente.cdvdd = tbvendedor.cdvdd
join tbvendas 
	on tbvendedor.cdvdd = tbvendas.cdvdd
where tbvendas.status = 'Concluído'
group by tbvendedor.cdvdd
order by valor_total_vendas 
limit 1