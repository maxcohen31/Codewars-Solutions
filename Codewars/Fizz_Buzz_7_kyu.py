def fizzbuzz(n):
    values = [i for i in range(1, n+1)]
    
    for idx in range(len(values)):
        if values[idx] % 3 == 0 and values[idx] % 5 != 0:
            values[idx] = "Fizz"
        elif values[idx] % 5 == 0 and values[idx] % 3 != 0:
            values[idx] = "Buzz"
        elif values[idx] % 3 == 0 and values[idx] % 5 == 0:
            values[idx] = "FizzBuzz"
    return values

    



print(fizzbuzz(10))