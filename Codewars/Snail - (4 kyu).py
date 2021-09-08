def snail(arr):
    snail_arr = []
    go_right, go_left, up, down = len(arr[0]), 0, 0, len(arr) 
    if len(arr) == 0:
        return [[]]
    while go_left < go_right and up < down:
        for i in range(go_left, go_right):
            snail_arr.append(arr[up][i])
        up += 1
        for i in range(up, down):
            snail_arr.append(arr[i][go_right - 1])
        go_right -= 1     
        for i in range(go_right - 1, go_left - 1, -1):
            snail_arr.append(arr[down-1][i])
        down -= 1
        for i in range(down -1, up - 1, -1):
            snail_arr.append(arr[i][go_left])
        go_left += 1    
    return snail
        
        
array = [[1,2,3],
         [4,5,6],
         [7,8,9]] 
   
print(snail(array))


