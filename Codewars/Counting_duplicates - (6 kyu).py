# Counting duplicates

from collections import Counter

def duplicate_count(text):
    
    new_text = list(text.lower())
    counter_new_text = Counter(new_text)
    counter_dup = 0
    
    for key, value in counter_new_text.items():
        if value > 1:
            counter_dup += 1
    return counter_dup        

