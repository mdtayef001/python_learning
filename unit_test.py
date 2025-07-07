def total_xp(level, xp_to_add):
    current_level = level * 100
    player_total_xp = current_level + xp_to_add
    return player_total_xp


print(total_xp(1, 100))     
print(total_xp(2, 250))    
print(total_xp(170, 590))  