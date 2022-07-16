def sum_of_digits(digits):
    try:
        str_digits = str(digits)
        sum_ = [sum(int(digit) for digit in str_digits)]
        if len(str_digits) == 0:
            return ''
        elif len(str_digits) == 1:
            return f'{str_digits} = {str_digits}'
        elif len(str_digits) > 1:
            op = ' + '.join(str_digits)
            for n in str_digits:
                return f'{op} = {sum_[0]}'
    except ValueError as e:
        return False
    
print(sum_of_digits('123'))