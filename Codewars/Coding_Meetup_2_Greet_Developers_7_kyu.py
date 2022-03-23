def greet_developers(lst): 
    for person in lst:
        person['greeting'] = f"Hi {person['firstName']}, what do you like the most about {person['language']}?"
    return lst

list1 = [
  { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
  { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' } 
]

print(greet_developers(list1))