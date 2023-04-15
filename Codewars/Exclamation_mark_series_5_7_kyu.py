"""  
Exclamation marks series #5: Remove all exclamation marks from the end of words
"""
from re import sub
def remove(s: str) -> str:
    return sub(r"\b!{1,}", "", s)
    
    
