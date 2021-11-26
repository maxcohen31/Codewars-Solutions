/* Oh you may not think I'm pretty,
But don't judge on what you see,
I'll eat myself if you can find
A smarter hat than me. */

SELECT *
FROM students
WHERE (students.quality1 = 'evil') AND (students.quality2 = 'cunning')
OR (students.quality1 = 'brave') AND (students.quality2 <> 'evil')
OR (students.quality1 = 'studious') OR (students.quality2 = 'intelligent')
OR (students.quality1 = 'hufflepuff') OR (students.quality2 = 'hufflepuff')
ORDER BY students.id;