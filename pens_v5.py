import random
import pen_function
import direction_function
import itertools

# [name, pen_ability]
team_1 = [
['mane', 95],
['salah', 96],
['jota', 81],
['thiago', 87],
['keita', 79],
['fabinho', 86],
['robertson', 76],
['van dijk', 84],
['matip', 66],
['alexander arnold', 88],
['alisson', 64, 89],
]

# Sort Team 1 into descending order of pen ability
t1_ordered = sorted(team_1, key=lambda item: item[1], reverse=True)


team_2 = [
['havertz', 91],
['werner', 87],
['lukaku', 83],
['jorginho', 97],
['kovacic', 85],
['kante', 81],
['chilwell', 79],
['rudiger', 73],
['silva', 77],
['james', 84],
['arrizabalaga', 53, 82],
]

# Sort Team 2 into descending order of pen ability
t2_ordered = sorted(team_2, key=lambda item: item[1], reverse=True)

# Create penalty order of alternating teams
penalty_order = [None]*(len(t1_ordered)+len(t2_ordered))
penalty_order[::2] = t1_ordered
penalty_order[1::2] = t2_ordered

# Set the goalkeeper ability
t1_gk_ability = team_1[10][2]
t2_gk_ability = team_2[10][2]

# Initialise the score, how many pens taken, how many to go and the score difference.
team_1_score = 0
team_2_score = 0
team_1_taken = 0
team_2_taken = 0

pens_remaining = 5
score_difference = 0

# Loop through each of the first 10 takers (5 on each team)
for player in penalty_order[:10]:

	# Team 1 faces Team 2 goalkeeper and vice versa
	if player in team_1:
		gk_ability = t2_gk_ability
	elif player in team_2:
		gk_ability = t1_gk_ability

	# Describe the taker
	if player in team_1:
		print(f"\n\n\n{player[0].title()}, Pen Ability - {player[1]}")
	elif player in team_2:
		print(f"\n{player[0].title()}, Pen Ability - {player[1]}")

	# Determine the shot/save directions and result of the penalty
	shot_direction, save_direction = direction_function.shot_direction()
	pen_result = pen_function.pen_result(shot_direction, save_direction, player, gk_ability)

	# Print the result and uupdate the score/number of pens taken
	if player in team_1 and pen_result == 'goal':
		team_1_score += 1
		team_1_taken += 1
	elif player in team_1 and pen_result == 'no_goal':
		team_1_score += 0
		team_1_taken += 1
	elif player in team_2 and pen_result == 'goal':
		team_2_score += 1
		team_2_taken += 1
	elif player in team_2 and pen_result == 'no_goal':
		team_2_score += 0
		team_2_taken += 1

	# Print the score
	print(f"Liverpool - {team_1_score}/{team_1_taken} | {team_2_score}/{team_2_taken} - Chelsea")

	# Determine if the shootout is won and should stop. If it is won, print winner and score
	team_2_pens_remaining = 5 - team_2_taken
	team_1_pens_remaining = 5 - team_1_taken
	team_2_score_difference = team_1_score - team_2_score
	team_1_score_difference = team_2_score - team_1_score
	if team_2_pens_remaining < team_2_score_difference or team_1_pens_remaining < team_1_score_difference:
		if team_1_score > team_2_score:
			print(f"\nLiverpool win {team_1_score} - {team_2_score}.")
		elif team_2_score > team_1_score:
			print(f"\nChelsea win {team_1_score} - {team_2_score}.")	
		break

# Determine if teams are tied after 5 takers each and sudden death is needed
if team_1_score == team_2_score:

	# Create new list starting at 6th pair of takers
	pen_order_sudden_death = penalty_order[10:] + penalty_order[:10]

	# Loop through the takers infinitely until the win condition is met
	for player in itertools.cycle(pen_order_sudden_death):
		if player in team_1:
			gk_ability = t2_gk_ability
		elif player in team_2:
			gk_ability = t1_gk_ability
		if player in team_1:
			print(f"\n\n\n{player[0].title()}, Pen Ability - {player[1]}")
		elif player in team_2:
			print(f"\n{player[0].title()}, Pen Ability - {player[1]}")
		shot_direction, save_direction = direction_function.shot_direction()
		pen_result = pen_function.pen_result(shot_direction, save_direction, player, gk_ability)
		if player in team_1 and pen_result == 'goal':
			team_1_score += 1
			team_1_taken += 1
		elif player in team_1 and pen_result == 'no_goal':
			team_1_score += 0
			team_1_taken += 1
		elif player in team_2 and pen_result == 'goal':
			team_2_score += 1
			team_2_taken += 1
		elif player in team_2 and pen_result == 'no_goal':
			team_2_score += 0
			team_2_taken += 1
		print(f"Liverpool - {team_1_score}/{team_1_taken} | {team_2_score}/{team_2_taken} - Chelsea")
		team_2_score_difference = team_1_score - team_2_score
		team_1_score_difference = team_2_score - team_1_score
		if team_1_taken == team_2_taken and team_1_score_difference != 0:
			if team_1_score > team_2_score:
				print(f"\nLiverpool win {team_1_score} - {team_2_score}.")
			elif team_2_score > team_1_score:
				print(f"\nChelsea win {team_1_score} - {team_2_score}.")	
			break
