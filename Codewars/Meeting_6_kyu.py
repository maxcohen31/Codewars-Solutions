def meeting(s):
    result = []
    new_s = s.upper().split(';')
    return new_s[0]
    for i in new_s:
        first, last = i.split(':')[0], i.split(':')[1]
        result.append(f"({last}, {first})")
    return ''.join(sorted(result))
        
    
    
    
    
s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(meeting(s))
