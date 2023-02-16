-- Script that prints the average temperatures (in Farehnheit) by city ordered by descending temperature
SELECT 'city', AVG('value') AS 'avg_temp'
FROM 'temperatures'
GROUP BY `city`
ORDER BY `avg_temp` DESC;
