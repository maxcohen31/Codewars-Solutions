def get_average(lst): 
    result = 0
    number_of_partecipants = len(lst)
    for person in lst:
        for k, v in person.items():
            if k == 'age':
                result += (v / number_of_partecipants)
    return round(result)


list1 = [
  { 'firstName': 'Maria', 'lastName': 'Y.', 'country': 'Cyprus', 'continent': 'Europe', 'age': 30, 'language': 'Java' },
  { 'firstName': 'Victoria', 'lastName': 'T.', 'country': 'Puerto Rico', 'continent': 'Americas', 'age': 70, 'language': 'Python' },
]
print(get_average(list1))