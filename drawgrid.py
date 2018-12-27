import turtle as t

def hline(start,color,pensize):
	t.pendown()
	t.pensize(pensize)
	t.color(color)
	#t.right(90)
	t.forward(start)
	t.backward(start)
	t.end_fill()
	t.penup()

def vline(start,color,pensize):
	t.pendown()
	t.pensize(pensize)
	t.color(color)
	t.right(90)
	t.forward(start)
	t.backward(start)
	t.right(270)
	t.penup()

def drawhgrid():
	# Horozontal line at 0,0
	

	t.penup()
	t.goto(0,200)
	t.write((0,200), True)
	hline(400,'yellow',.2)
	hline(-400,'yellow',.2)

	t.penup()
	t.goto(0,-200)
	t.write((0,-200), True)
	hline(400,'yellow',.2)
	hline(-400,'yellow',.2)

	t.penup()
	t.goto(0,100)
	t.write((0,100), True)
	hline(400,'yellow',.2)
	hline(-400,'yellow',.2)

	t.penup()
	t.goto(0,-100)
	t.write((0,-100), True)
	hline(400,'yellow',.2)
	hline(-400,'yellow',.2)

	t.penup()
	t.goto(0,0)
	t.write((0,0), True)
	hline(400,'yellow',2)
	hline(-400,'yellow',2)

	t.penup()
	t.goto(0,300)
	t.write((0,300), True)
	hline(400,'yellow',.2)
	hline(-400,'yellow',.2)

	t.penup()
	t.goto(0,-300)
	t.write((0,-300), True)
	hline(400,'yellow',.2)
	hline(-400,'yellow',.2)

	t.penup()
	t.goto(0,-50)
	t.write((0,-50), True)
	hline(400,'yellow',.2)
	hline(-400,'yellow',.2)

	t.penup()
	t.goto(0,50)
	t.write((0,50), True)
	hline(400,'yellow',.2)
	hline(-400,'yellow',.2)
	
	t.penup()
	t.goto(0,-150)
	t.write((0,-150), True)
	hline(400,'yellow',.2)
	hline(-400,'yellow',.2)

	t.penup()
	t.goto(0,150)
	t.write((0,150), True)
	hline(400,'yellow',.2)
	hline(-400,'yellow',.2)

	t.penup()
	t.goto(0,-250)
	t.write((0,-250), True)
	hline(400,'yellow',.2)
	hline(-400,'yellow',.2)

	t.penup()
	t.goto(0,250)
	t.write((0,250), True)
	hline(400,'yellow',.2)
	hline(-400,'yellow',.2)
	

def drawvgrid():
	#vertical lines at 0
	t.penup()
	t.goto(0,0)
	vline(400,'red',2)
	vline(-400,'red',2)
	
	#vertical lines at 50
	t.penup()
	t.goto(50,0)
	vline(-400,'red',.2)
	vline(400,'red',.2)

		#vertical lines at 100
	t.penup()
	t.goto(100,0)
	vline(-400,'red',.2)
	vline(400,'red',.2)

			#vertical lines at -200
	t.penup()
	t.goto(-200,0)
	vline(-400,'red',.2)
	vline(400,'red',.2)

			#vertical lines at -100
	t.penup()
	t.goto(-100,0)
	vline(-400,'red',.2)
	vline(400,'red',.2)

			#vertical lines at -50
	t.penup()
	t.goto(-50,0)
	vline(-400,'red',.2)
	vline(400,'red',.2)

			#vertical lines at 200
	t.penup()
	t.goto(200,0)
	vline(-400,'red',.2)
	vline(400,'red',.2)

			#vertical lines at 150
	t.penup()
	t.goto(150,0)
	vline(-400,'red',.2)
	vline(400,'red',.2)

			#vertical lines at -150
	t.penup()
	t.goto(-150,0)
	vline(-400,'red',.2)
	vline(400,'red',.2)

			#vertical lines at 250
	t.penup()
	t.goto(250,0)
	vline(-400,'red',.2)
	vline(400,'red',.2)

			#vertical lines at -250
	t.penup()
	t.goto(-250,0)
	vline(-400,'red',.2)
	vline(400,'red',.2)

			#vertical lines at 300
	t.penup()
	t.goto(300,0)
	vline(-400,'red',.2)
	vline(400,'red',.2)

			#vertical lines at -300
	t.penup()
	t.goto(-300,0)
	vline(-400,'red',.2)
	vline(400,'red',.2)