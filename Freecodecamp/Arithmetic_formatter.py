# Arithmetic formatter

def arithmetic_formatter(problems, status = True):
    
    first_line= ''
    second_line = ''
    separators = ''
    result = ''
    
    # Checking the lenght of the problems array
    
    if len(problems) > 5:
        return "Error: Too many problems"
    
    # Splitting up the array
    
    for index in problems:
         
        first_number = index.split()[0]
        operator = index.split()[1]
        second_number = index.split()[2]
        sum_numbers = ''
        
        # Checking for conditions to be valid
        
        if len(first_number) > 4 or len(second_number) > 4:
            return 'Error: Numbers cannot contain more than four digits'
        if operator == '/' or operator == '*':
            return "Error: operator must be '+' or '-'"
        if not first_number.isdigit() or not second_number.isdigit():
            return 'Error: Numbers must only contain digits'
        
        # Addition and Subtraction 
        
        if operator == '+':
            sum_numbers = str(int(first_number) + int(second_number))
        elif operator == '-':
            sum_numbers = str(int(first_number) - int(second_number)) 
        
        # Arranging     
            
        max_lenght = max(len(first_number), len(second_number)) + 2
        top_line = str(first_number).rjust(max_lenght)
        bottom = operator + str(second_number).rjust(max_lenght - 1)
        answer = str(sum_numbers).rjust(max_lenght)
        signs = '-' * max_lenght
        
        
        first_line += top_line + '     '
        second_line += bottom + '     '
        separators += signs + '     '
        result += answer + '     '
        
        # Checking for the status to be True or False
        
    if status == True:
        arranged_problems = first_line + '\n' + second_line + '\n' + separators + '\n' + result
    else:
        arranged_problems = first_line + '\n' + second_line + '\n' + separators
                   
    return arranged_problems    
                                
print(arithmetic_formatter(['32 + 698', '3802 - 2', '45 + 43', '123 + 49']))


                        
                        