-- Script to list all records with a score in the table second_table of the database hbth_Oc_O in my MySQL server

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
