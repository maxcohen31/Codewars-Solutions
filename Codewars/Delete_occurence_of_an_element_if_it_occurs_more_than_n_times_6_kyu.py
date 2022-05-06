def delete_nth(order,max_e):

    result = []
    dict_ = {k:0 for k in order}
    
    for n in order:
        if dict_[n] < max_e:
            dict_[n] += 1
            result.append(n)
    return result

print(delete_nth([20,37,20,21], 1))
print(delete_nth([1,1,3,3,7,2,2,2,2], 3)) # [1, 1, 3, 3, 7, 2, 2, 2]

