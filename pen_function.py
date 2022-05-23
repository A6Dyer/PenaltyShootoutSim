def pen_result(shot_direction, save_direction, player, gk_ability):
	import random

	# Goalkeeper goes the right way
	if shot_direction == save_direction:
		# player has higher taking ability than goalkeeper's saving ability
		if player[1] > gk_ability:
			# Make the on target probability more relaistic for lower rated players
			ontarget_probability = player[1] * (2 - (1/(player[1]/10))) 
			# Set max and min probabilities
			if ontarget_probability > 99:
				ontarget_probability = 99
			if ontarget_probability < 1:
				ontarget_probability = 1
			# Determine if shot is on target. If miss, print/return outcome
			if random.randint(1,100) <= ontarget_probability:
				shot_ontarget = True
				if shot_ontarget:
					# Determine probability of shot being saved
					# If gk ability and pen ability are equal, 33% chance of saving (Max)
					# If gk ability 1 and pen ability 99, 1% chance (Min)
					save_probability = int(round((100 - (player[1] - gk_ability))/3))
					# Determine if saved or scored and print/return outcome
					if random.randint(1,100) > save_probability:
						print("Scores! The goalkeeper guessed right but couldn't quite get there.")
						return 'goal'
					else:
						print("Saved! A well struck penalty but an even better save.")
						return 'no_goal'
			else:
				print("Missed!")
				return 'no_goal'
		# Goalkeeper has higher save ability than player's taking ability or equal
		else:
			ontarget_probability = player[1] * (2 - (1/(player[1]/10))) 
			if ontarget_probability > 99:
				ontarget_probability = 99
			if ontarget_probability < 1:
				ontarget_probability = 1
			if random.randint(1,100) <= ontarget_probability:
				shot_ontarget = True
				if shot_ontarget:
					# Determine the probability of shot being scored
					# If gk ability and pen ability are equal, 66% chance of scoring
					# If gk ability 99 and pen ability 1, 1% chance of scoring
					score_probability = int(round((100 - (gk_ability - player[1]))/1.5))
					if random.randint(1,100) > score_probability:
						print("Saved! A nice height for the goalkeeper.")
						return 'no_goal'
					else:
						print("Scores! The goalkeeper nearly got to that!")
						return 'goal'
			else:                                                                         
				print("Missed!")
				return 'no_goal'

	# Goalkeeper dives the incorrect way
	elif shot_direction != save_direction:
		ontarget_probability = player[1] * (2 - (1/(player[1]/10))) 
		if ontarget_probability > 99:
			ontarget_probability = 99
		if ontarget_probability < 1:
			ontarget_probability = 1
		# Player just needs to put it on target to score
		if random.randint(1,100) < ontarget_probability: 
			print("Scores! He sent the goalkeeper the wrong way.")
			return 'goal'
		else:
			print("Misses! With the goal at his mercy.")
			return 'no_goal'