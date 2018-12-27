def guess_check(guess,answer):
	global score
	still_guessing = True
	attempt=0
	while still_guessing and attempt<2:
		if guess.upper()==answer.upper():
			print('good job, you are correct')
			score=score+1
			still_guessing=False
		elif attempt<1:
			guess=input('sorry that is wrong, try again')
			attempt=attempt+1



score=0
guess=input('which of these eats leaves?\n\
A)whale\nB)sea otter\nC)rhinoceros\ntype A,B, or C')
guess_check(guess, 'B')

