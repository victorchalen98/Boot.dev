def remove_nonints(nums):
    new_list = []
    for i in nums:
        if type(i) == int:
            new_list.append(i)
    return new_list
