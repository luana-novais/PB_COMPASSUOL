
SELECT DISTINCT 
a.nome

from autor a
left join livro li
	on li.autor = a.codautor 
left join editora ed 
	on li.editora = ed.codeditora 
left join endereco en
	on ed.endereco = en.codendereco 
WHERE en.estado not in ('PARANÁ', 'RIO GRANDE DO SUL', 'SANTA CATARINA')	
order by a.nome ASC 


