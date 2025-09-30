def find_min(nums):
    my_infinity = float("inf")

    for number in nums:
        if number < my_infinity:
            my_infinity = number
    return my_infinity
