def disemvowel(s):
    vowels = 'aeiouAEIOU'
    for v in vowels:
        s = s.replace(v, '')
    return s

p = 'This website is for losers LOL!'
print(disemvowel(p))
