def anagrams(word, words):
    anag = []
    for i in words:
        if sorted(i) == sorted(word):
            anag.append(i)
    return anag




def anagrams2(word, words):
    return [w for w in words if sorted(w) == sorted(word)]




print(anagrams('aabb',['aabb','bbaa','ccaa','baba']))
     
        
  