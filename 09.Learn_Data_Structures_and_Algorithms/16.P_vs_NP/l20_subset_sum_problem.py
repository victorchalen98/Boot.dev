def subset_sum(nums, target):
    return find_subset_sum(nums, target, len(nums) - 1)


def find_subset_sum(nums, target, index):
    if target == 0:
        return True

    if index < 0:
        return False

    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)

    without_current = find_subset_sum(nums, target, index - 1)

    with_current = find_subset_sum(nums, target - nums[index], index - 1)

    return without_current or with_current
