import re
def count_smileys(arr):
    faces = ''.join(arr)
    smiley = re.findall('[:;][-~]?[D)]', faces)
    return len(smiley)


def count_smileys2(arr):
    smileys = [":)", ";)", ":~)", ";~)", ":-)", ";-)", ":D", ";D", ":~D", ";~D", ":-D", ";-D"]
    faces = 0
    if not arr:
        return 0
    for face in arr:
        if face in smileys:
            faces += 1
    return faces
