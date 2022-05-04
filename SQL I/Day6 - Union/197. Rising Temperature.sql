# Write your MySQL query statement below
select tod.id from weather tod, weather yest where tod.temperature > yest.temperature and datediff(tod.RecordDate, yest.RecordDate)=1; 