SELECT P.NOME, DAY(PAG.DT_PAGAMENTO) as DIA_MES, C.VALOR_PARCELA
FROM PESSOAS P INNER JOIN PAGAMENTO PAG ON P.ID = PAG.PESSOA_ID
INNER JOIN CONTRATOS C ON P.CONTRATO_ID = C.ID
WHERE P.INADIMPLENTE <> N

SELECT P.NOME, (C.VALOR_PARCELA*C.PARCELAS) as VALOR_TOTAL
FROM PESSOA P INNER JOIN CONTRATO C ON P.CONTRATO_ID = C.ID
INNER JOIN PAGAMENTO PAG ON P.DT_COMPLETO = PAG.DT_PAGAMENTO
