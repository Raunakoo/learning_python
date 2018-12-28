import random as ran

abc = "abcdefghijklmnopqrstuvwxyzdsw"

letter1 = abc[ran.randrange(len(abc))]
letter2 = abc[ran.randrange(len(abc))]
letter3 = abc[ran.randrange(len(abc))]

word = letter1 + letter2 + letter3
print(word)