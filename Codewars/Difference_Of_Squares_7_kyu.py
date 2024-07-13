def difference_of_squares(n: int) -> int:
    sum_squares = sum([i**2 for i in range(n+1)])
    square_of_sum = pow(sum([i for i in range(n+1)]), 2)

    return square_of_sum - sum_squares



if __name__ == "__main__":
    print(difference_of_squares(10))
