-- Query to list datas and the number of duplicates


SELECT score, COUNT(*) as number FROM second_table GROUP BY score;
