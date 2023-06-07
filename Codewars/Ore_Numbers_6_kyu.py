import scipy

def is_ore(n: int) -> bool:
    divisors = [d for d in range(1, n+1) if n % d == 0]
    sum_ = 0
    for idx, val in enumerate(divisors):
        sum_ += 1 / val
    harmonic_mean = len(divisors) / sum_
    return round(harmonic_mean, 6).is_integer() # I don't like it :D

if __name__ == "__main__":
    print(is_ore(2970))


# ALternative method using Scipy
from scipy import stats

def is_ore(n):
    def divisors(n):
        return list(filter(lambda x: n % x is 0, range(1, n + 1)))
    return round(stats.hmean(divisors(n)), 7).is_integer()
