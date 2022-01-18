def DNA_strand(dna):
    dna_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    result = ""
    for letter in dna:
        for k, v in dna_dict.items():
            if letter == k:
                result += v    
    return result
    
    
a = 'AAAA'    
print(DNA_strand(a))