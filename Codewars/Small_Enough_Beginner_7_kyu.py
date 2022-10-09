def small_enough(array, limit):
    for i in range(len(array)):
        if array[i] > limit:
            return False
    return True

# ALternative Solution
def small_enough(array, limit):
    return max(array) <= limit