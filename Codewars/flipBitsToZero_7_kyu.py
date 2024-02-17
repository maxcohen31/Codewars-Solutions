def bin_str(input):
    flips_needed = 0
    last_seen = '0'
    for c in input:
        if last_seen != c:
            flips_needed += 1
            last_seen = c
    return flips_needed


if __name__ == "__main__":
    print(bin_str("0101"))
