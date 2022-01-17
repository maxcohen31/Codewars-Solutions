# from string import ascii_lowercase
# def high(x: str) -> str:
#     x = x.split()
#     alpha = ascii_lowercase
#     max_value = 0
#     scoring_for_words = []
#     for word in x:
#         total = 0
#         for letter in word:
#             if letter in alpha:
#                 total += ord(letter) - 96        
    
#         if total > max_value:
#             max_value = total    
#             result = word
#     return result        

# Alternative Solution
from string import ascii_lowercase
def high(x):
    letter_worth = {letter: int(index) for index, letter in enumerate(ascii_lowercase, start=1)}
    words = x.split()
    total = []
    for word in words:
        count = 0
        for letter in word:
            count += letter_worth.get(letter)
        total.append(count)
    return words[total.index(max(total))]

print(high('b aa'))

