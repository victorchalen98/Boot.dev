def num_possible_orders(num_posts):
    result = 1
    for i in range(2, num_posts + 1):
        result *= i
    return result

