def divide_list(nums, divisor):
    valor = 0
    divided_list = []

    for num in nums:
        valor = num / divisor
        divided_list.append(valor)
    return divided_list
    

