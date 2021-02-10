# Mumbling

def accum(s):
    
    counter = 0
    answer = ''
    for char in s:
        counter += 1
        answer += char.upper()
        for i in range(counter - 1):
            answer += char.lower()
        if counter < len(s):
            answer += '-'
    return answer
    
    
# Alternative solution     
def accum2(s):
    
    answer = ''
    for i in range(len(s)):
        answer += s[i] * (i + 1) + '-'
    return answer[:-1]    
   
   
   
   
   
    
               
        
            




