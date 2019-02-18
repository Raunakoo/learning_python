
import random
import turtle as t


t.bgcolor('yellow')

caterpillar=t.Turtle()	

caterpillar.shape('square')
caterpillar.resizemode('user')
caterpillar.shapesize(1,1)
caterpillar.color('brown')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

caterpillar2=t.Turtle()	
caterpillar2.shape('square')
caterpillar2.color('blue')
caterpillar2.speed(0)
caterpillar2.penup()
caterpillar2.hideturtle()

leaf=t.Turtle()
leaf_shape=((0,0),(14,2),(18,6),(20,20),(6,18)\
	,(2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

game_started=False
text_turtle=t.Turtle()
text_turtle.color('green')
text_turtle.write('Press SPACE BAR to start',align='center',\
	font=('helectiva',20,'bold'))
text_turtle.hideturtle()

score_turtle=t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

score2_turtle=t.Turtle()
score2_turtle.hideturtle()
score2_turtle.speed(0)

def outside_window(caterpillar):
	left_wall= -t.window_width()/2	
	right_wall=t.window_width()/2
	top_wall=t.window_width()/2
	bottom_wall= -t.window_width()/2
	(x,y)=caterpillar.pos()
	outside=\
	x<left_wall or \
	x>right_wall or \
	y<bottom_wall or \
	y>top_wall
	return outside

	

def Game_over(name, score):
	
	caterpillar.color('yellow')
	leaf.color('yellow')
	caterpillar2.color('yellow')

	t.penup()
	t.hideturtle()
	t.color('green')
	t.write('Game Over Thank You '+str(name)+' won, scored '\
		+str(score),align='center', font=\
		('ariel',30,'normal'))

def display_score1(current_score):
	print('display score1 function called',current_score,\
		t.window_width())

	score_turtle.clear()
	score_turtle.penup()
	
	x=(t.window_width()/2)+150
	y=(t.window_width()/2)+150
	score_turtle.setpos(200,200)
	score_turtle.color('green')
	score_turtle.write('player1 score = '+str(current_score), font=\
		 ('ariel',20,'bold'))

def display_score2(current_score):
	print('display score2 function called',current_score,\
		t.window_width())

	score2_turtle.clear()
	score2_turtle.penup()
	
	x=(t.window_width()/2)-250
	y=(t.window_width()/2)-250
	score2_turtle.setpos(-200,-200)
	score2_turtle.color('green')
	score2_turtle.write('player2 score = '+ str(current_score)\
		, font=('ariel',20,'bold'))


def Place_leaf():
	print('place leaf function called')
	leaf.hideturtle()
	leaf.setx(random.randint(-200,200))
	leaf.sety(random.randint(-200,200))	
	leaf.showturtle()

def start_game():
	global game_started
	if game_started:
		return
	game_started=True
	
	score1=0
	score2=0 
	text_turtle.clear()
	
	caterpillar_speed=2
	caterpillar2_speed=2

	caterpillar_length=3
	caterpillar2_length=3
	caterpillar.shapesize(1,caterpillar_length,1)
	caterpillar.showturtle()
	
	

	caterpillar2.shapesize(1,caterpillar2_length,1)
	caterpillar2.setheading(180)
	caterpillar2.showturtle()

	
	Place_leaf()

	while True:
		caterpillar.forward(caterpillar_speed)
		caterpillar2.forward(caterpillar2_speed)
		
		if caterpillar.distance(leaf)<20:
			Place_leaf()
			caterpillar_length=caterpillar_length+1
			caterpillar.shapesize(1,caterpillar_length,1)	
			caterpillar_speed=caterpillar_speed+1
			score1=score1+10
			display_score1(score1)


		if caterpillar2.distance(leaf)<20:
			Place_leaf()
			caterpillar2_length=caterpillar2_length+1
			caterpillar2.shapesize(1,caterpillar2_length,1)
			caterpillar2_speed=caterpillar2_speed+1
			score2=score2+10
			display_score2(score2)

		if outside_window(caterpillar) or \
					outside_window(caterpillar2):
			if score1 > score2:
				Game_over('player1', score1)
			elif score1 <score2:
				Game_over('player2', score2)
			elif score1==score2:
				t.penup()
				t.hideturtle()
				t.color('green')
				t.write('Thank You! \n IT IS A DRAW!!'\
					,align='center', font=\
					('ariel',30,'normal'))
			break

def move_up():
	if caterpillar.heading()==0	or caterpillar.heading()==180:
		caterpillar.setheading(90)
def move_down():
	if caterpillar.heading()==0	or caterpillar.heading()==180:
		caterpillar.setheading(270)
def move_left():
	if caterpillar.heading()==90	or caterpillar.heading()==270:
		caterpillar.setheading(180)
def move_right():
	if caterpillar.heading()==90	or caterpillar.heading()==0:
		caterpillar.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,"Up")
t.onkey(move_right,"Right")
t.onkey(move_down,"Down")
t.onkey(move_left,"Left")

def caterpillar2_move_up():
	if caterpillar2.heading()==0	or caterpillar2.heading()==180:
		caterpillar2.setheading(90)
def caterpillar2_move_down():
	if caterpillar2.heading()==0	or caterpillar2.heading()==180:
		caterpillar2.setheading(270)
def caterpillar2_move_left():
	if caterpillar2.heading()==90	or caterpillar2.heading()==270:
		caterpillar2.setheading(180)
def caterpillar2_move_right():
	if caterpillar2.heading()==90	or caterpillar2.heading()==0:
		caterpillar2.setheading(0)



t.onkey(caterpillar2_move_up,'w')
t.onkey(caterpillar2_move_right,"d")
t.onkey(caterpillar2_move_down,"s")
t.onkey(caterpillar2_move_left,"a")

t.listen()
t.mainloop()

start_game()


t.hideturtle()
t.done()
