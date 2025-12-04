import math
def log_scale(data, base):
    new_list = []

    for i in data:
        log_num = math.log(i, base)
        new_list.append(log_num)

    return new_list

