def comp(array1, array2):
    try:
        squared = sorted([n * n for n in array1])
        return squared == sorted(array2)
    except TypeError:
        return False
