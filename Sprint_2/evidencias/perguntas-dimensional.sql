-- Qual a receita total gerada pelas locações? 
SELECT totalLocacao 
from fato_locacao fl 



-- Como essa receita está distribuída entre carros, clientes e vendedores?
-- total por carro 

SELECT dc.marcaCarro , dc.modeloCarro, sum(fl.totalLocacao) as 'total_receita'
from fato_locacao fl 
join dim_carro dc 
on fl.idCarro = dc.idCarro 
GROUP BY dc.marcaCarro , dc.modeloCarro
ORDER by fl.totalLocacao DESC 

-- total por cliente
SELECT dc.nomeCliente, dc.estadoCliente, sum(fl.totalLocacao) as 'total_receita'
FROM fato_locacao fl 
join dim_clientes dc 
on fl.idCliente = dc.idCliente 
GROUP BY dc.nomeCliente, dc.estadoCliente
ORDER by fl.totalLocacao DESC 

-- total por vendedores
SELECT dv.nomeVendedor,dv.estadoVendedor, sum(fl.totalLocacao) as 'total_receita'
from fato_locacao fl 
join dim_vendedor dv 
on fl.idVendedor = dv.idVendedor 
GROUP BY dv.nomeVendedor, dv.estadoVendedor 
ORDER by fl.totalLocacao DESC 

-- total por ano
SELECT dd.ano , SUM(fl.totalLocacao) AS receitaTotal
FROM fato_Locacao fl
JOIN dim_data dd ON fl.dataLocacao = dd.data
GROUP BY dd.ano 


