def bubblesort_once(l):
    nums = list(l)

    for _ in range(1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

x = [9, 7, 5, 3, 1, 2, 4, 6, 8]
print(bubble_sort(x))