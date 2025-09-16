def total_xp(level, xp_to_add):
    level_to_xp = level * 100
    result = level_to_xp + xp_to_add
    return result

my_level = 1
my_xp_to_add = 100

intro = total_xp(my_level, my_xp_to_add)
print(f"Player is level {my_level} and gain {my_xp_to_add} xp, the player have {intro} total xp")