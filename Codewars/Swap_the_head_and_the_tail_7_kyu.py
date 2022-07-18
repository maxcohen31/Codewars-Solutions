def swap_head_tail(arr):
    if len(arr) % 2 == 0:
        first = arr[0:len(arr) // 2]
        second = arr[len(arr)// 2:]    
        return second + first
    if len(arr) % 2 != 0:
        first_odd = arr[0:len(arr) - (len(arr)// 2) - 1]
        second_odd = arr[(len(arr)//2) + 1:]    
        return second_odd + [arr[len(arr)//2]] + first_odd   
    
a = [6, 7, 8, 9, 10, 12]    
print(swap_head_tail(a))