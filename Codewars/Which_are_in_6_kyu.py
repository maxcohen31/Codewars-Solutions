def in_array(a, b):
    words = []
    for word in b:
        for word2 in a:
            if word2 in word:
                words.append(word2)  
    return sorted(list(set(words)))


    
a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]   
print(in_array(a1, a2))
