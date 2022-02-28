def count_developers(lst):
    developers = 0
    for person in lst:
        if person['language'] == 'JavaScript' and person['continent'] == 'Europe':
            developers += 1
    return developers

# One liner
def count_developers(lst):
    return sum(x["language"] == "JavaScript" and x["continent"] == "Europe" for x in lst) 
    
lst1 = [
  { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
  { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
  { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
  { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
]

list2 = [
          { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 19, 'language': 'HTML' },
          { 'firstName': 'Lukas', 'lastName': 'R.', 'country': 'Austria', 'continent': 'Europe', 'age': 89, 'language': 'HTML' }
        ]    
print(count_developers(lst1))

