-- List all records with a name value ordered by score DESC
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
