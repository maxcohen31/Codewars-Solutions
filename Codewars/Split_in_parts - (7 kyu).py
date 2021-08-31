import itertools
def split_in_parts(s, part_length): 
    iterator_new_string = [iter(s)] * part_length
    result =  list(itertools.zip_longest(*iterator_new_string, fillvalue=''))
    return ' '.join([''.join(i) for i in result])
    
# Alternative Solution    
from textwrap import wrap    
def split_in_parts2(s, part_length):
    return ' '.join(wrap(s, part_length))

# alternative Solution
def split_in_parts3(s, part_length):  
    return ' '.join(s[i:i+part_length] for i in range(0, len(s), part_length))


