def remove_duplicates(spells):
    seen = set()
    unique_list = []

    for spell in spells:
        if spell not in seen:
            seen.add(spell)
            unique_list.append(spell)
    
    return unique_list
