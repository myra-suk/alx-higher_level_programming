-- Score that prints the scores and names of those whose score >= 10 from the table second_table in the database hbtn_0c_0 in the MySQL server 
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
