def exponential_growth(n, factor, days):
    growth = [n]
    for _ in range(days):
        growth.append(growth[-1] * factor)
    return growth

