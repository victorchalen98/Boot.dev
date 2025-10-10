def join_strings(strings):
    result = ""
    for i in range(len(strings)):
        result += strings[i]
        if i < len(strings) - 1:  
            result += ","
    return result




