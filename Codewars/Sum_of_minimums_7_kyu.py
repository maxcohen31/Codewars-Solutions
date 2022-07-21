def sum_of_minimums(n):
      sum_m = 0
      for i in n:
            sum_m = sum_m + min(i)
      return sum_m


x = [[7,9,8,6,2],
     [6,3,5,4,3],
     [5,8,7,4,5]]

print(sum_of_minimums(x))


