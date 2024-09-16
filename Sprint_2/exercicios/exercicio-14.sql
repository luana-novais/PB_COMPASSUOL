gasto medio por estado

SELECT 
	estado,
	ROUND(AVG(qtd * vrunt),2) as 'gastomedio'
from tbvendas t
WHERE status = 'Concluído'
group by estado 
ORDER by gastomedio DESC 