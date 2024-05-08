from typing import List

def collatz(n: int) -> List[int]:
    col = [n]
    while(n != 1):
        if n % 2 == 0:
            col.append(n//2)
            n //= 2
        elif n % 2 == 1:
            col.append(3*n + 1)
            n = 3 * n + 1
    return col


def longest_collatz(input_array: List[int]) -> int:
    collection_collatz = []
    for i in input_array:
        collection_collatz.append(len(collatz(i)) - 1)

    number_and_collatz = zip(input_array, collection_collatz)
    return sorted(list(number_and_collatz), key=lambda x: x[1], reverse=True)[0][0]

