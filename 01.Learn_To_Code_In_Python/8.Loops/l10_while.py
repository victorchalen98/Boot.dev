def regenerate(current_health, max_health, enemy_distance):
    while (current_health < max_health) & (enemy_distance > 3):
        current_health += 1
        enemy_distance -= 2
    return current_health
