SELECT 
a.nome,
a.codautor,
a.nascimento,
COUNT(li.titulo) as quantidade
from autor a 
left join livro li
	on li.autor = a.codautor 
group by a.codautor
order by a.nome ASC 