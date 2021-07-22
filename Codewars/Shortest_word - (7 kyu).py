def find_short(s):
    w = s.split()
    w.sort(key=len)
    return len(w[0])

def find_short2(s):
    return min(len(x) for x in s.split())

f = "bitcoin take over the world maybe who knows perhaps"


