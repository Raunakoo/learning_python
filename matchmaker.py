import random
import time
from tkinter import Tk, Button, DISABLED

def show_symbol(x,y):
	global first
	global previousX, previousY
	buttons[x,y] ['text']=button_symbols[x,y]
	buttons[x,y].update_idletasks()
	if first:
		previousX=x
		previousY=y
		first=False
	elif previousX != x or previousY !=y :	
		if buttons[previousX, previousY]['text'] !=buttons[x,y]\
		['text']:
			time.sleep(0.0)
			buttons[previousX, previousY]['text']=''
		else:
			buttons[previousX, previousY]['command']=DISABLED
			buttons[x,y]['command']=DISABLED

		first=True	
			



root = Tk()

root.title('matchmaker')
root.resizable(height=True, width=True)
buttons={}
first=True
previousX=0
previousY=0
button_symbols={}
symbols=[u'\U0000265a',u'\U0000265a',
		u'\u2702', u'\u2702',
		u'\U0000265c', u'\U0000265c',
		u'\u2705', u'\u2705',
		u'\u270A', u'\u270A',
		u'\u2708', u'\u2708',
		u'\u2709', u'\u2709', 
		u'\u270B', u'\u270B', 
		u'\u270c', u'\u270c',
		u'\u270F', u'\u270F', 
		u'\u2728', u'\u2728',
		u'\u2716', u'\u2716']

#print('before',symbols)
random.shuffle(symbols)
#print('after shuffle',symbols.pop())


for x in range(6):
	for y in range(4):
		button=Button(command=lambda x=x, y=y: show_symbol(x,y),\
			width=10, height=10)
		button.grid(column=x, row=y)
		buttons[x,y]=button
		button_symbols[x, y]= symbols.pop()


root.mainloop()

