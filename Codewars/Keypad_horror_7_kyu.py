def computer_to_phone(numbers):
    result = ''
    computer = '0789456123'
    phone = '0123456789'
    new_keypad = dict(zip(list(computer), list(phone)))
    for number in list(numbers):
        for k, v in new_keypad.items():
            if number == k:
                result += v
    return result                

print(computer_to_phone('92'))