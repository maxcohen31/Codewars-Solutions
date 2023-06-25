SELECT DISTINCT(c.student_id), s.name, (scince.score - math.score) AS score_difference
FROM courses c
JOIN students s ON c.student_id = s.id
JOIN courses scince ON c.student_id = scince.student_id AND scince.course_name = 'Science'
JOIN courses math ON c.student_id = math.student_id AND math.course_name = 'Math'
WHERE scince.score > math.score
ORDER BY 3 DESC, 1
