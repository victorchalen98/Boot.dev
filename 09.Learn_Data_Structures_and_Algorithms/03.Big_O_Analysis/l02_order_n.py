def find_max(nums):
    max = float("-inf")

    for numbers in nums:
        if numbers > max:
            max = numbers
    return max

