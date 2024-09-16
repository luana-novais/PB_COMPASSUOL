CREATE table tb_clientes (
	idCliente       integer PRIMARY key,
  	nomeCliente     varchar(100),
  	cidadeCliente   varchar(40),
  	estadoCliente   varchar(40),
  	paisCliente     varchar(40)
);
CREATE table tb_combustivel (
 	idCombustivel   integer primary key,
  	tipoCombustivel varchar(20)
);
CREATE table tb_carro (
	idCarro         integer primary key,
  	classiCarro     varchar(50),
  	marcaCarro      varchar(80),
  	modeloCarro     varchar(80),
  	anoCarro        text,
  	idCombustivel   integer,
  	foreign key (idCombustivel) references tb_combustivel (idCombustivel)
);
CREATE table tb_vendedor(
	idVendedor      integer primary key,
  	nomeVendedor    varchar(15),
  	sexoVendedor    smallint,
  	estadoVendedor  varchar(40)
);
CREATE table tb_locacao2(
	idLocacao       integer primary key, 
  	idCliente       integer,
  	idCarro         integer,
	dataLocacao     datetime,
  	horaLocacao     time,
  	qtdDiaria       integer,
  	vlrDiaria       decimal(18,2),
  	dataEntrega     datetime,
  	horaEntrega     time,
  	idVendedor      integer,
  	kmCarro         integer,
  	foreign key(idCliente) references tb_clientes(idCliente),
  	foreign key(idCarro) references tb_carro (idCarro),
  	foreign key(idVendedor) references tb_vendedor(idVendedor)
);

-- Inserindo dados na tabela Clientes
INSERT or IGNORE INTO tb_clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

-- Inserindo dados na tabela Carro
INSERT or IGNORE INTO tb_carro (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT DISTINCT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM tb_locacao;

-- Inserindo dados na tabela Combustivel
INSERT or IGNORE INTO tb_combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao;

-- Inserindo dados na tabela Vendedor
INSERT or IGNORE INTO tb_vendedor(idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

-- Inserindo dados na tabela Locação
INSERT or IGNORE INTO tb_locacao2 (idLocacao,kmCarro,idCliente,idCarro,idVendedor,dataLocacao,horaLocacao,qtdDiaria,vlrDiaria,dataEntrega,horaEntrega)
select DISTINCT idLocacao,kmCarro,idCliente,idCarro,idVendedor,dataLocacao,horaLocacao,qtdDiaria,vlrDiaria,dataEntrega,horaEntrega
from tb_locacao 


DROP TABLE IF EXISTS tb_locacao




