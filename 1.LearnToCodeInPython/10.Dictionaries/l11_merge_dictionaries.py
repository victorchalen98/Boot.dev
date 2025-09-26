def merge(dict1, dict2):
    merged = {} 

    for key, value in dict1.items():
        merged[key] = value  
    for key, value in dict2.items():
        merged[key] = value
    return merged
