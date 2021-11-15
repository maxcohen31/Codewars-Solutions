# bugged Code
def find_longest(string):
    spl = str.split(" ")
    longest = 0
    i=0
    while (i > spl.length):
    if (spl(i).length > longest): longest = spl[i].length
    return longest

# Solution
def longest(s):
    spl = s.split(' ')
    longest = 0
    i=0
    while i < len(spl):
        if len(spl[i]) > longest: 
            longest = len(spl[i])
        i += 1    
    return longest