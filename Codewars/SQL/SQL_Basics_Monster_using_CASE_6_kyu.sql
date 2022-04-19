/*  SQL  */
SELECT top_half.id AS id, top_half.heads AS heads, top_half.arms AS arms, bottom_half.legs AS legs, bottom_half.tails AS tails,
CASE  
    WHEN heads > arms OR tails > legs THEN 'BEAST'
    ELSE 'WEIRDO'
END AS species
FROM top_half, bottom_half
WHERE top_half.id = bottom_half.id
ORDER BY species;