def take_magic_damage(health, resist, amp, spell_power):
    spell_damage = (spell_power * amp) - resist
    damage_take = health - spell_damage
    return damage_take


print(take_magic_damage(100, 10, 1.5, 40))
print(take_magic_damage(100, 20, 2.0, 30))
print(take_magic_damage(50, 25, 1.0, 20))
print(take_magic_damage(80, 0, 2.0, 50))
