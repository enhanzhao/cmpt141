#Enhan Zhao 11097118



r = 1
p1_score = 0
p2_score = 0

while p1_score < 3 and p2_score < 3:
	
	print ("Round", r)
	p1_finger = int(input ("How many fingers did player 1 put out?"))
	p2_finger = int(input ("How many fingers did player 2 put out?"))
	sum_fingers = int(p1_finger + p2_finger)
	p1_guess = int(input ("What is player 1's guess of sum of all the fingers?"))
	p2_guess = int(input ("What is player 2's guess of sum of all the fingers?"))
		
	if p1_guess == sum_fingers and p2_guess == sum_fingers:
		p1_score = p1_score + 1
		p2_score = p2_score + 1
		r = r + 1
		print ("Both players guessed right! The score now is", p1_score, p2_score)
		if p1_score == 3 and p2_score == 3:
			print ("Its a tie!")
		elif p1_score == 3 and p2_score == 0:
			print ("Player 1 wins a glorious victory!")
		elif p1_score == 0 and p2_score == 3:
			print ("Player 2 wins a glorious victory!")
		elif p1_score == 3 and p2_score < 3:
			print ("Player 1 wins!")
		elif p1_score < 3 and p2_score == 3:
			print ("Player 2 wins!")
		elif p1_score == 2 and p2_score == 2:
			print ("Both players only need one more point to win!")
		elif p1_score == 2 and p2_score < 2:
			print ("Player 1 has two points, one more to victory!")
		elif p1_score < 2 and p2_score == 2:
			print ("Player 2 has two points, one more to victory!")
		else:
			pass

	elif p1_guess == sum_fingers and p2_guess != sum_fingers:
		p1_score = p1_score + 1
		r = r + 1
		print ("Player 1 gets a score! The score now is", p1_score, p2_score)
		if p1_score == 3 and p2_score == 3:
			print ("Its a tie!")
		elif p1_score == 3 and p2_score == 0:
			print ("Player 1 wins a glorious victory!")
		elif p1_score == 0 and p2_score == 3:
			print ("Player 2 wins a glorious victory!")
		elif p1_score == 3 and p2_score < 3:
			print ("Player 1 wins!")
		elif p1_score < 3 and p2_score == 3:
			print ("Player 2 wins!")
		elif p1_score == 2 and p2_score == 2:
			print ("Both players only need one more point to win!")
		elif p1_score == 2 and p2_score < 2:
			print ("Player 1 has two points, one more to victory!")
		elif p1_score < 2 and p2_score == 2:
			print ("Player 2 has two points, one more to victory!")
		else:
			pass

	elif p1_guess != sum_fingers and p2_guess == sum_fingers:
		p2_score = p2_score + 1
		r = r + 1
		print ("Player 2 gets a score! The score now is", p1_score, p2_score)
		if p1_score == 3 and p2_score == 3:
			print ("Its a tie!")
		elif p1_score == 3 and p2_score == 0:
			print ("Player 1 wins a glorious victory!")
		elif p1_score == 0 and p2_score == 3:
			print ("Player 2 wins a glorious victory!")
		elif p1_score == 3 and p2_score < 3:
			print ("Player 1 wins!")
		elif p1_score < 3 and p2_score == 3:
			print ("Player 2 wins!")
		elif p1_score == 2 and p2_score == 2:
			print ("Both players only need one more point to win!")
		elif p1_score == 2 and p2_score < 2:
			print ("Player 1 has two points, one more to victory!")
		elif p1_score < 2 and p2_score == 2:
			print ("Player 2 has two points, one more to victory!")
		else:
			pass
	
	elif p1_guess != sum_fingers and p2_guess != sum_fingers:
		r = r + 1
		print ("Neither player guessed right!")
		
