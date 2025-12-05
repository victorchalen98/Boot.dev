def count_names(list_of_lists, target_name):
    count = 0
    for sub_list in list_of_lists:
        for names in sub_list:
            if names == target_name:
                count += 1
    return count

