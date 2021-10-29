from string import ascii_lowercase
def solve(st: str):
    st = sorted(st)
    new_st = ''.join(st)     
    if new_st in ascii_lowercase:
        return True
    return False         
      
print(solve(''))