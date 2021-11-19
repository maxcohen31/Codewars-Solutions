SELECT INITCAP(elves.firstname) || ' ' || INITCAP(elves.lastname) AS shortlist
FROM elves
WHERE elves.firstname LIKE '%tegil%' OR elves.lastname LIKE '%astar%'