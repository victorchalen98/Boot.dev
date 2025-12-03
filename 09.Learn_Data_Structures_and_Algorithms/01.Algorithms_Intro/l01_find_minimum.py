def find_minimum(nums):
    minimun = float("inf")
    if len(nums) <= 0:
        return None
    
    for numbers in nums:
        if numbers < minimun:
            minimun = numbers
    return minimun

