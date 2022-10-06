def sort_by_length(arr):
    result = []
    words_length = list(zip([len(word) for word in arr], arr))
    sorting = sorted(words_length, key=lambda x: x[0])
    return [w for idx, w in sorting]
    


a = ["Telescopes", "Glasses", "Eyes", "Monocles"]
b = ['beg', 'i', 'life', 'to']
print(sort_by_length(b))