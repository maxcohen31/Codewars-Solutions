SELECT connections.id AS id, network(connections.ip_address) AS first_address, broadcast(connections.ip_address) AS last_address
FROM connections
ORDER BY connections.id