"""
    Your goal is to implement the method meanVsMedian which accepts an odd-length array 
    of integers and returns one of the following:

    'mean' - in case mean value is larger than median value
    'median' - in case median value is larger than mean value
    'same' - in case both mean and median share the same value
    Reminder: Median

    Array will always be valid (odd-length >= 3)
"""

def mean_vs_median(arr):

    mean = sum(sorted([x for x in arr])) // len(arr)
    median = sorted(arr)[len(arr) // 2]
 
    return "median" if median > mean else "mean" if mean > median else "same"
    

if  __name__ == "__main__":
    print(mean_vs_median([7, 14, -70]))
    print(mean_vs_median([-10, 20, 5]))
