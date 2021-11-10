def how_much_i_love_you2(nb_petals):
    module = {
              0: 'not at all',
              1: 'I love you', 
              2: 'a little',
              3: 'a lot',
              4: 'passionately',
              5: 'madly'
            }
    operation = nb_petals % 6
    for k, v in module.items():
        if operation == k:
            return v
print(how_much_i_love_you2(3))