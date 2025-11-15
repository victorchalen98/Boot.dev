def sum_nested_list(lst):
    total_size = 0
    for item in lst:
        if isinstance(item, (int)):
            total_size += item
        elif isinstance(item, list):
            len_list = sum_nested_list(item)
            total_size += len_list
    return total_size
