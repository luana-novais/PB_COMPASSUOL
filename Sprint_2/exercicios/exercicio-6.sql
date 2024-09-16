SELECT 
	a.codautor,
	a.nome,
	count(li.titulo) as quantidade_publicacoes
from autor a 
inner join livro li
	on li.autor = a.codautor 
group by a.codautor 
HAVING COUNT(li.titulo) = (
    SELECT MAX(publicacoes)
    FROM (
        SELECT COUNT(li2.titulo) AS publicacoes
        FROM autor a2
        INNER JOIN livro li2 ON li2.autor = a2.codautor
        GROUP BY a2.codautor
    ) AS subquery
)
order by quantidade_publicacoes DESC 
