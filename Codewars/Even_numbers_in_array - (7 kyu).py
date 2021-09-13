def even_numbers2(arr, n):
    return [number for number in arr if number % 2 == 0][-n:]

