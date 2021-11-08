def count_letters_and_digits(s):
    counter = 0
    for element in s:
        if element.isdigit() or element.isalpha():
            counter += 1
    return counter
