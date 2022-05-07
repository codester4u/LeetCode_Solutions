SELECT a.name, IFNULL(SUM(b.distance), 0) AS travelled_distance
FROM Users AS a
LEFT JOIN Rides AS b
ON a.id = b.user_id
GROUP BY a.name
ORDER BY travelled_distance DESC, name ASC;