WITH gastos_totais as (	
	SELECT 
		cdcli,
		nmcli,
		SUM(vrunt * qtd) as gastos
	FROM tbvendas
	group by nmcli, cdcli 
	ORDER by gastos DESC 
)
SELECT 
    cdcli,
    nmcli,
    gastos
FROM gastos_totais
WHERE gastos = (
    SELECT MAX(gastos)
    FROM gastos_totais
)
ORDER BY gastos DESC