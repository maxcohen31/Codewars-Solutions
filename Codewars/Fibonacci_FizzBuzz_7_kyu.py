def fibs_fizz_buzz(n):
    if n == 1:
        return [1]
    a, b = 1, 1
    fibo_fuz = [a, b]

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        fibo_fuz.append(c)
    
    for idx in range(len(fibo_fuz)):
        if fibo_fuz[idx] % 3 == 0 and fibo_fuz[idx] % 5 == 0:
            fibo_fuz[idx] = "FizzBuzz"
        elif fibo_fuz[idx] % 3 == 0:
            fibo_fuz[idx] = "Fizz"
        elif fibo_fuz[idx] % 5 == 0:
            fibo_fuz[idx] = "Buzz"
    return fibo_fuz



print(fibs_fizz_buzz(20)) 
# [1,1,2,"Fizz","Buzz",8,13,"Fizz",34,"Buzz",89,"Fizz",233,377,"Buzz","Fizz",1597,2584,4181,"FizzBuzz"]