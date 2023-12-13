from typing import List

def reverse_middle(lst: List[int]) -> List[int]:
    middle_index = (len(lst) // 2) - 1
    if(len(lst) % 2 == 0):
        return lst[middle_index:middle_index + 2][::-1]
    return lst[middle_index:middle_index + 3][::-1]

x = [1, 2, 3, 4, 5]
if __name__ == "__main__":
    print(reverse_middle(x))
