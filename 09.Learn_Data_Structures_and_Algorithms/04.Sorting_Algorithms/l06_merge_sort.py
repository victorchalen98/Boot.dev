def merge_sort(nums):
    if len(nums) < 2:
        return nums

    sorted_left_side = nums[:len(nums)//2]
    sorted_right_side = nums[len(nums)//2:]
    
    left_side = merge_sort(sorted_left_side)
    right_side = merge_sort(sorted_right_side)

    return merge(left_side, right_side)

def merge(first, second):
    final = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else: 
            final.append(second[j])
            j += 1

    while i < len(first):
        final.append(first[i])
        i += 1
    
    while j < len(second):
        final.append(second[j])
        j += 1
    return final

