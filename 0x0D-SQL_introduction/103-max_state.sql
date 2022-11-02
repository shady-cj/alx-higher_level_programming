-- A script that displays the max temperature of each state

SELECT state, MAX(value) AS Avg_temp FROM temperatures GROUP BY state ORDER BY state;
