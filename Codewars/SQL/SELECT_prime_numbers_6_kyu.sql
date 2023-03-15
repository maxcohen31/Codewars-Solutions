SELECT p.primes AS prime
FROM GENERATE_SERIES(2, 100) AS  p (primes)
WHERE NOT EXISTS(
  SELECT p2 FROM GENERATE_SERIES(2, 100) AS p2 (primes2)
  WHERE p.primes % p2.primes2 = 0 AND p.primes > p2.primes2
  )
ORDER BY prime ASC


-- ALternative solution: Wilson's theorem
SELECT * FROM GENERATE_SERIES(2, 100) AS prime WHERE (((prime - 1)!) + 1) % prime = 0