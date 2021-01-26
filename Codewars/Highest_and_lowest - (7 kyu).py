

def high_and_low(numbers):
  # must split the numbers, convert them to integers and print the max and min of list
  numbers = numbers.split()
  numbers = [int(i) for i in numbers]
  return str(max(numbers))+" "+str(min(numbers))



