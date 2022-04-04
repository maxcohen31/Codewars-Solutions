def grid(N):
    grid_ = ''
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    if 0 < N < 13:
        for i in range(N):
            grid_ += ('\n' +' '.join([alphabet[i] for i in range(i,N+i)]))     
        return grid_[1:]   
    elif N >= 13:
        for i in range(N):
            grid_ += ('\n' + ' '.join([alphabet[(i+j)%26] for j in range(N)]))
        return grid_
    elif N < 0:
        return None
    else:
        return ''
     

print(grid(4))
