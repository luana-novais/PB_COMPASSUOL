SELECT 
    t.nmpro ,
    t2.cdpro 
FROM tbvendas t
INNER JOIN tbestoqueproduto t2 
    ON t.cdpro = t2.cdpro
WHERE t.dtven >= '2014-02-03'
  AND t.dtven <= '2018-02-02'
  AND t.status = 'Concluído'
GROUP BY t2.cdpro, t.nmpro
HAVING COUNT(t.cdpro) = (
    SELECT MAX(vendas_produtos)
    FROM (
        SELECT COUNT(cdpro) AS vendas_produtos
        FROM tbvendas
        WHERE dtven >= '2014-02-03'
          AND dtven <= '2018-02-02'
          AND status = 'Concluído'
        GROUP BY cdpro
    ) AS subquery
)
ORDER BY COUNT(t.cdpro) DESC
