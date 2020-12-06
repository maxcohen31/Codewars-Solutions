# A program to find the n-terms of the Fibonacci sequence
def fibonacci(n):
    n_1 = 0
    n_2 = 1
    print(n_1)
    print(n_2)
    for x in range(2, n):
        n_3 = n_1 + n_2
        n_1 = n_2
        n_2 = n_3
        print(n_3)

fibonacci(4)















