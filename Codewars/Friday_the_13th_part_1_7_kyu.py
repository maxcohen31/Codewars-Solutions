def kill_count(counselors: list[str, int], jason: int) -> str:
    killed = []
    
    for name, intel in counselors:
        if intel < jason:
            killed.append(name)
            
    return killed


p = [["Mike", 7],["Alysa", 3]]
j = 7
print(kill_count(p, j))