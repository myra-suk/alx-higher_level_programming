-- Script that lists all records where the name value is not null and has a value in the table second
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
