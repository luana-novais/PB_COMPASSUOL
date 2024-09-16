SELECT count(li.titulo) AS quantidade,
ed.nome,
en.estado, 
en.cidade
from livro li
left join editora ed
	on li.editora = ed.codeditora 
left join endereco en 
	on ed.endereco = en.codendereco 
group by ed.nome 
order by quantidade DESC 
limit 5