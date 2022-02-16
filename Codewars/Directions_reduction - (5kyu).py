def dirReduc(arr):
    if len(arr) == 1:
        return arr[0] 
    else:
        new_string = ' '.join(arr)  
        reduction = new_string.replace('NORTH SOUTH', '').replace('SOUTH NORTH', '').replace('EAST WEST', '').replace('WEST EAST', '')
        new_arr = reduction.split()
        if len(new_arr) < len(arr):
            return dirReduc(new_arr)
        else:
            return new_arr
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]    
print(dirReduc(a))