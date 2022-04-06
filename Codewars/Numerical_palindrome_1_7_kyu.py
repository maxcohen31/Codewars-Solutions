def palindrome(num):
    return num == int(str(num)[::-1]) if isinstance(num, int) and num > 0 else 'Not valid'