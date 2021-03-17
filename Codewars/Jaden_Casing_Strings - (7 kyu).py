# Jaden Casing String

def to_jaden_case(s):
    
    splitting = s.split()
    result = []
    for letter in splitting:
        case = letter.capitalize()
        result.append(case)
    final = ' '.join(result)
    return final    


quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))