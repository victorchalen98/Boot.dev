def power_set(input):
    if not input:
        return [[]]

    all_subsets = [[]]

    for element in input:
        new_subsets = []
        for subset in all_subsets:
            new_subset = subset + [element]
            new_subsets.append(new_subset)
        all_subsets.extend(new_subsets)

    return all_subsets

