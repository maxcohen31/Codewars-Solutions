SELECT pokemon.pokemon_name, (pokemon.str * multipliers.multiplier) AS modifiedStrength, multipliers.element
FROM pokemon
JOIN multipliers ON pokemon.element_id = multipliers.id
WHERE (pokemon.str * multipliers.multiplier) >= 40
ORDER BY modifiedStrength DESC;