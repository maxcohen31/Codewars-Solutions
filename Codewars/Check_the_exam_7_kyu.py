def check_exam(arr1: list[str], arr2: list[str]) -> int:
    result = 0

    # zip quiz and answer together
    comparison = list(zip(arr1, arr2))
    for vote1, vote2 in comparison:
        if vote1 == vote2:
            result += 4
        elif vote1 != vote2:
            if vote2 == "":
                result += 0 
            else:
                result -= 1

    return result if result > 0 else 0
        


  
print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))


