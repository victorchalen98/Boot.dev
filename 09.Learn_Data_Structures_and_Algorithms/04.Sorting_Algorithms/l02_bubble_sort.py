def bubble_sort(nums):
    list_nums = nums[:]
    swapping = True
    end = len(list_nums)

    while swapping:
        swapping = False
        for i in range(1, end):
            if list_nums[i-1] > list_nums[i]:
                list_nums[i - 1], list_nums[i] = list_nums[i], list_nums[i - 1]
                swapping = True
        end -= 1
    return list_nums

