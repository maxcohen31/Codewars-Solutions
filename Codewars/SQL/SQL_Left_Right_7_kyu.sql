SELECT LEFT(repo.project, repo.commits) AS project, RIGHT(repo.address, repo.contributors) AS address
FROM repositories repo