def dont_give_me_five(start,end):
    # your code here
    result = []
    list_of_numb = list(range(start, end+1))
    for n in list_of_numb:
        if '5' in str(n):
            result.append(n)
    return len(list_of_numb) - len(result)

print(dont_give_me_five(4, 17))