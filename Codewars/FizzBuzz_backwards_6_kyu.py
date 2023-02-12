def reverse_fizz_buzz(array: list) -> tuple:
    w1, w2 = 1, 1
    if "Fizz" in array:
        w1 = array.index("Fizz")
    elif "FizzBuzz" in array:
        w1 = array.index("FizzBuzz")
    if "Buzz" in array:
        w2 = array.index("Buzz")
    else:
        w2 = array.index("FizzBuzz")
    
    return (w1 + 1, w2 + 1)

print()