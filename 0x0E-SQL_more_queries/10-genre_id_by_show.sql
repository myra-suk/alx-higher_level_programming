-- Srip that lists all te shows in the database hbtn_0d_tvshows that have at least one genre linked and reords are listed by ascending v_shows.title and tv_show_genres.genre_id
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       INNER JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
  ORDER BY s.`title`, g.`genre_id`;
