-- List the records of the same score in the table
SELECT score,COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
