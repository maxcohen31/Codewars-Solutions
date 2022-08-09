def triangular(n):
    return (n * (n + 1)) // 2 if n > 0 else 0

def to_freud(sentence):
    sex = 'sex ' * len(sentence.split())
    return sex[0:len(sex)-1]
print(to_freud('This is a s'))