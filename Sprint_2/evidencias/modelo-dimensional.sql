CREATE view dim_clientes as
select	idCliente,
		nomeCliente,
  		cidadeCliente,
  		estadoCliente,
  		paisCliente
 from tb_clientes   

CREATE view dim_carro as
select	idCarro,                  
  		classiCarro,     
  		marcaCarro,      
  		modeloCarro,     
  		anoCarro  
from tb_carro  

CREATE view dim_vendedor as
select	idVendedor,
  		nomeVendedor,
  		sexoVendedor,
  		estadoVendedor
 from tb_vendedor  	
  	
CREATE view fato_locacao as
select	idLocacao, 
  		idCliente,
  		idVendedor,
  		idCarro,
		dataLocacao,
  		qtdDiaria,
  		vlrDiaria,
  		(qtdDiaria * vlrDiaria) as totalLocacao 
from tb_locacao  		

CREATE table dim_data (
	idData integer primary key,
	data TEXT,
	ano text,
	mes TEXT,
	dia text
)

INSERT INTO dim_data (data,ano,mes,dia)
SELECT DISTINCT 
	dataLocacao as data,
	substr(dataLocacao, 1, 4) AS ano,
    substr(dataLocacao, 5, 2) AS mes,
    substr(dataLocacao, 7, 2) AS dia
FROM tb_locacao 

INSERT INTO dim_data(data,ano,mes,dia)
SELECT DISTINCT 
	dataEntrega as "data" ,
	substr(dataEntrega, 1, 4) AS ano,
    substr(dataEntrega, 5, 2) AS mes,
    substr(dataEntrega, 7, 2) AS dia
FROM tb_locacao 
