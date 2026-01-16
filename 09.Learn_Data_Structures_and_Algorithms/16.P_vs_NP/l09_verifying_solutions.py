def get_num_guesses(length):
    total = 0
    for i in range(1, length + 1):
        total += 26 ** i
    return total

