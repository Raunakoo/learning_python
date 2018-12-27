import random
import string
adjectives=['green','blue','sleepy','black','round','flat','brave']
nouns=['cucumber','onion','zebra','lion']
print('welcome, pick which funny and\
 hack proof password you like')
adjective=random.choice(adjectives)
noun=random.choice(nouns)
number=random.randrange(0,120)
special_character=random.choice(string.punctuation)
password=adjective+noun+str(number)+special_character
print('do you like it?your new password is:',password)
print('do you like it?your new password is: %s'%password)