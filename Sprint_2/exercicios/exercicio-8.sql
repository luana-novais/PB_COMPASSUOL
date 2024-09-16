select 
t.cdvdd,
t2.nmvdd
from tbvendas t 
left join tbvendedor t2 
	on t.cdvdd = t2.cdvdd 
where t.status = 'Concluído'
group by t.cdvdd, t2.nmvdd 
HAVING count(t.cdven) = (
	select max(vendas)
	from (
		select COUNT(cdven) as vendas
		from tbvendas t
		where status = 'Concluído'
		group by cdvdd) as subquery
)
order by count(t.cdven) DESC 


