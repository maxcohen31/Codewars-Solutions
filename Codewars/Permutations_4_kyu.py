from itertools import permutations as permutations_of
def permutations(string):
    result = []
    perm = [''.join(i) for i in permutations_of(string)]
    return set(perm)   
    
s = 'aabb'
print(permutations(s))