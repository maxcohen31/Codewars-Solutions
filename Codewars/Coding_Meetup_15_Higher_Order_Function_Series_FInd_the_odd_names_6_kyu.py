def find_odd_names(lst): 
    result = []
    for item in lst:
        result.append(item['firstName'])
    
    names = []
    
    for name in result:
        names.append(sum(map(ord, name)))
   
    zipped = list(zip(lst, names))
    
    answer = []
    for i, j in zipped:
        if int(j) % 2 != 0:
            answer.append(i)
    return answer


list1 = [
          { 'firstName': 'Aba', 'lastName': 'N.', 'country': 'Ghana', 'continent': 'Africa', 'age': 21, 'language': 'Python' },
          { 'firstName': 'Abb', 'lastName': 'O.', 'country': 'Israel', 'continent': 'Asia', 'age': 39, 'language': 'Java' }
        ]

print(find_odd_names(list1))