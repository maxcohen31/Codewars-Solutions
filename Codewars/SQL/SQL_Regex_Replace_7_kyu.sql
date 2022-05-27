SELECT repositories.project,
repositories.commits,
repositories.contributors,
REGEXP_REPLACE(repositories.address, '\d', '!', 'g') AS address
FROM repositories;