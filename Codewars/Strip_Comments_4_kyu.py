def solution(string, markers):
   
    # Works with the majority of tests, presents some issues. Bad code though
    
    # new = ""
    # to_delete = []
    # splitting_escape = string.split('\n')
    # for mark in markers:
    #     if mark in string:
    #         to_delete.append(string.index(mark))

    # if len(to_delete) == 2:
        
    #     partial = []
    #     for idx, val in enumerate(string):
    #         if idx == to_delete[0] and idx == to_delete[1]:
    #             partial.append(string[idx:])
        
    #     result = string.replace(partial, '').rstrip(' ')
    #     partial = ''.join([string[i] for i in range(to_delete[0],string.index('\n'))])
    #     partial2 = ''.join([string[i] for i in range(to_delete[1],len(string))])
    #     new = string.replace(partial, '').replace(partial2, '')
    #     first_escape_index = new.index('\n')
    #     first_part = ''.join(new[idx] for idx in range(0, first_escape_index+1))
    #     first_part = first_part[0:first_escape_index]
    #     result = first_part + new[first_escape_index+1:-1].rstrip(' ')
    
    # elif len(to_delete) == 1:
    #     partial = ''
    #     for idx, val in enumerate(string):
    #         if idx == to_delete[0]:
    #             partial = string[idx:]
        
    #     result = string.replace(partial, '').rstrip(' ')
    # return result
    

    splitting_string = string.split('\n')
    for elem in markers:
        splitting_string = [i.split(elem)[0].strip() for i in splitting_string]
    return '\n'.join(splitting_string)
    
    
    
x = "apples, pears # and bananas\ngrapes\nbananas !apples" 
y = "apples, pears # and bananas\ngrapes\navocado @apples"
v = "apples, pears § and bananas\ngrapes\navocado *apples"
m = ["#", "!"]
m1 = ['@', '!']
m2 = ["*", "§"]
print(solution(x, m))
print(solution(v, m2))
    

    
    
