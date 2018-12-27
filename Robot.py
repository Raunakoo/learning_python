import turtle as t
import drawgrid as d
 # setup screen size
t.setup (800, 800, 0, 0)


t.bgcolor('blue')
t.shape('turtle')
t.speed('fastest')

def rectangle(horizontal,vertical,color):
	
	t.pendown()
	t.pensize(5)
	t.color(color)
	t.begin_fill()
	for counter in range(1, 3):
		t.forward(horizontal)
		t.right(90)
		t.forward(vertical)
		t.right(90)
	t.end_fill()
	t.penup()

d.drawvgrid()

d.drawhgrid()	

# Below code draws the feet
t.penup()
t.goto(-200,-200)	
rectangle(90,40,'yellow')
t.penup()
t.goto(100,-200)
rectangle(90,40,'yellow')

#Below code draws robot legs
#y, x
t.goto(-120,-100)
rectangle(15,100,'lawn green')
t.goto(100,-100)
rectangle(15,100,'lawn green')
#below code draws body
t.penup()
# go to means vertical line start, vertical line end
t.goto(150,140)
rectangle(-300,250,'green')
#below code draws the arms
t.goto(100,0)
rectangle(90,30,'orange')
t.hideturtle()
t.done()