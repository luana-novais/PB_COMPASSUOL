SELECT  
	a.nome
from autor a 
left join livro li
	on li.autor = a.codautor 
group by a.codautor
HAVING COUNT(li.titulo) = 0 
 
