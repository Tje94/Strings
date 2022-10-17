# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_1 = 'Ruud Gullit'
player_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = f'{player_1} {goal_0}, {player_2} {goal_1}'
report = f'{player_1} scored in the {goal_0}nd minute\n{player_2} scored in the {goal_1}th minute'

player = 'Erwin Koeman'
start_first_name = player.find('E')
end_first_name = player.find('n')
first_name = player[:5]

start_last_name = player.find('K')
end_last_name = player.find('n', 6, -1)
last_name_len = len(player[6:])

name_short = player[0] + '.' + ' ' + player[6:]

chant_space = f'{first_name}! ' * len(first_name)
chant = chant_space.rstrip()
good_chant = chant[-1] != ' '
