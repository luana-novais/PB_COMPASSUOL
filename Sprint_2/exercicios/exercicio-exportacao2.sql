SELECT 
ed.codeditora as CodEditora,
ed.nome as NomeEditora,
count(li.titulo) AS QuantidadeLivros
from livro li
left join editora ed
	on li.editora = ed.codeditora 
left join endereco en 
	on ed.endereco = en.codendereco 
group by ed.nome 
order by QuantidadeLivros DESC 
limit 5