def binary_pyramid(m: int, n: int) -> str:
    #your code here
    bin_list = [int(bin(i)[2:]) for i in range(m, n+1)]
    return str(bin(sum(bin_list))[2:])


if __name__ == "__main__":
    print(binary_pyramid(1, 4))

    
