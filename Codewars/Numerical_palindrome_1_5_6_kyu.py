def you_are_not_that_guy_pal_trust_me_(pal: int) -> bool:
    return  str(pal) == str(pal)[::-1] if pal > 10 else False 


def palindrome(num: int, s: int) -> list:
    if isinstance(num, str) or isinstance(s, str) or num < 0 or s < 0:
        return 'Not valid'
    
    that_guy = []
    
    if num > 10 and you_are_not_that_guy_pal_trust_me_(num):
        that_guy.append(num)
    while len(that_guy) < s and s > 0:
        num += 1  
        if you_are_not_that_guy_pal_trust_me_(num) == True:
                    that_guy.append(num)
    return that_guy


# print(you_are_not_that_guy_pal_trust_me_(1))
print(palindrome('as', 4))