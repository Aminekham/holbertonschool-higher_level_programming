-- listing all the records
SELECT score, name FROM second_table
ORDER BY CASE WHEN score >= 10 THEN 1;