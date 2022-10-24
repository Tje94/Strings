player_1 = 'Ruud Gullit'
player_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = f'{player_1} {goal_0}, {player_2} {goal_1}'
report = f'{player_1} scored in the {goal_0}nd minute\n{player_2} scored in the {goal_1}th minute'

player = 'Erwin Koeman'
first_name = player[:player.find(' ')]

last_name = player[player.find(' ') +1:]
last_name_len = len(player[player.find(' ') +1:])

name_short = player[0] + '.' + ' ' + last_name

chant_space = f'{first_name}! ' * len(first_name)
chant = chant_space.rstrip()
good_chant = chant[-1] != ' '
