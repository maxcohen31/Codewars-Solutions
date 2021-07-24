def sum_triangular_numbers(n):
    sum_trian = 0
    if n < 0:
        return 0
    for i in range(n+1):
       sum_trian += i*(i+1) // 2
    return sum_trian  

print(sum_triangular_numbers(4))