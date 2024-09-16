select 
l.cod as 'CodLivro',
l.titulo,
l.autor as 'CodAutor',
a.nome as 'NomeAutor',
l.valor,
l.editora as 'CodEditora', 
e.nome as 'NomeEditora'
from livro l 
join autor a 
	on a.codautor = l.autor 
join editora e 
	on l.editora = e.codeditora
order by valor DESC 
LIMIT 10