def shot_direction():
	import random
	shot_direction = random.randint(1,3)                            # choose shot direction
	save_direction = random.randint(1,3)                            # choose save direction
	if shot_direction == 1:                                         # print which way the shot goes
		print("Shoots left")
	elif shot_direction == 2:
		print("Shoots down the middle")
	else:
		print("Shoots right")
	return shot_direction, save_direction