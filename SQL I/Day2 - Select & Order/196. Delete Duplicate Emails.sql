WITH cte AS (
SELECT Id, EMail, ROW_NUMBER() OVER(PARTITION BY Email ORDER BY Id) as row_num FROM Person)

DELETE FROM Person
WHERE Id IN (SELECT id FROM cte WHERE row_num > 1 )