def like_or_dislike(lst: list) -> str:
    status = "Nothing"
    for clic in lst:
        if clic != status:
            status = clic
        else:
            status = "Nothing"
    return status
    
x = ['Like', 'Like', 'Like']
a = ['Like', 'Like', 'Dislike', 'Like', 'Like', 'Like', 'Like', 'Dislike']
b = ['Like', 'Dislike', 'Dislike']
print(like_or_dislike(x))
print(like_or_dislike(a))
print(like_or_dislike(b))