def get_most_common_enemy(enemies_dict):
    if not enemies_dict:
        return None 
    
    max_count = -1
    most_common_enemy = None

    for enemy, count in enemies_dict.items():
        if count > max_count:
            max_count = count
            most_common_enemy = enemy

    return most_common_enemy
