def summed(nums):
    sum = 0
    if len(nums) == 0:
        return 0

    for i in nums:
        sum += i

    return sum
