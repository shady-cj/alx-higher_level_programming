-- Query to list datas and the number of duplicates


SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
