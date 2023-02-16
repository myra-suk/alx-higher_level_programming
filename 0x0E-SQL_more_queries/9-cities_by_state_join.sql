-- Scripts that lists all cities in the database hbtn_0d_usa and the records are listed in order of ascening cities' ID
SELECT c.`id`, c.`name`, s.`name`
  FROM `cities` AS c
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
