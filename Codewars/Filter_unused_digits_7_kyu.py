def unused_digits(*args) -> str:
    return ''.join([digit for digit in '0123456789' if digit not in ''.join(map(str,list(args)))])
