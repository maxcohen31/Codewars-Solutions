SELECT greetings.name, greetings.greeting, SUBSTRING(greetings.greeting FROM '#(\d+)') AS user_id 
FROM greetings;