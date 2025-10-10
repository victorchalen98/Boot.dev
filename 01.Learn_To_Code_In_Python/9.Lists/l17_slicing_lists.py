def get_champion_slices(champions):
    value1 = champions[2:]
    value2 = champions[0:-1]
    value3 = champions[::2]

    return value1, value2, value3

print(get_champion_slices)