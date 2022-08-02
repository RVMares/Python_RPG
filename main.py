legendary_monsters = ['Nemean Lion', 'Lernaean Hydra', 'Cerberus']
hercules_hit_points = 188
hercules_attack_power = 38
hercules_attack_dict = {
    'Unarmed Attack': -11,
    'Spear Melee Attack': -12,
    'Spear Ranged Attack': -12,
    'Longbow Ranged Attack': -7,
    'Healing Word': 7
}
nemean_lion_hit_points = 68
nemean_lion_attack_power = 25
nemean_lion_attack_dict = {
    'Bite': -9,
    'Claws': -12
}
hydra_hit_points = 172
hydra_attack_power = 25
hydra_attack_dict = {
    'Bite': -10,
    'Tail Swipe': -16
}
cerberus_hit_points = 168
cerberus_attack_power = 31
cerberus_attack_dict ={
    'Bite': -14,
    'Fire Breath': -32,
    'Scratch': -11
}

print('Welcome Great Hero!!!')
print('You have been tasked by King Eurystheus to complete your penance!')
print('You may be asking \"What penance, what did I do?\" I shall explain...')
print('It is not entirely your fault for Hera was jealous and drove you to madness!')
print('Alas, your beloved Megara was an innocent victim. You must avenge her and purify your sin!')
def start_RPG():
    game_start = input ('Are you up to the challenge? For you must slay the Nemean Lion! Defeat the Nine-Headed Hydra! And capture the guard dog of the underworld... Cerberus! Enter y/n: ')
    if game_start == 'y':
        print ('Make sure your weapons and mind are sharp! For the challenge begins!')
    else:
        print ('What is this? Are you defeated so quickly? Who can defeat the Mighty Hercules?')
        start_RPG()
start_RPG()
