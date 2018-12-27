
import random

lives=9
words=['apply','pyara','tooth','india','japan'\
			,'china', 'texas', 'idaho', 'spain', 'ocean'\
				,'mommy']
secret_word=random.choice(words)
clue=list('?????')
heart_symbol = u'\u2764'+' '
guessed_word_Correctly= False

def update_clue(guessed_letter,secret_word, clue):
	index=0
	while index<len(secret_word):
		if guessed_letter==secret_word[index]:
			clue[index]=guessed_letter
		index=index+1

while lives>0:
	print(clue)
	print('you have' +heart_symbol*lives,'lives left')
	guess=input('guess a letter or whole word:')	
	
	if guess==secret_word:
		guessed_word_Correctly=True
		break
	
	if guess in secret_word:
		update_clue(guess, secret_word, clue)
	else:
		print('sorry, you lose a life')
		lives=lives-1

if guessed_word_Correctly:
	print('good job, you won!The secret word was '+secret_word)
else:
	print('bad luck, you lost.The secret word was '+secret_word)	