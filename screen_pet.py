from tkinter import HIDDEN, NORMAL, Tk , Canvas


def toggle_eyes():
	current_color= c.itemcget(left_eye, "fill")
	new_color= c.body_color if current_color== "white" else "white"
	current_state= c.itemcget(left_pupil, "state")
	new_state = NORMAL if current_state == HIDDEN else HIDDEN
	c.itemconfigure(left_pupil, state=new_state)
	c.itemconfigure(right_pupil, state=new_state)
	c.itemconfigure(left_eye , fill=new_color)
	c.itemconfigure(right_eye, fill=new_color)


def	blinking_pet():
	toggle_eyes()
	root.after(250, toggle_eyes)
	root.after(3000, blinking_pet)

def toggle_pupils():
	if not c.eyes_crossed:
		c.move(left_pupil, 10, -5)
		c.move(right_pupil, -10, -5)
		c.eyes_crossed=True
	else:
		c.move(left_pupil, -10, 5)
		c.move(right_pupil, 10, 5)
		c.eyes_crossed=False

def tongue_toggle():
	if not c.tongue_out:
		c.itemconfigure(tip_tongue, state=NORMAL)
		c.itemconfigure(main_tongue, state=NORMAL)
		c.tongue_out=True
	else:
		c.itemconfigure(tip_tongue, state=HIDDEN)
		c.itemconfigure(main_tongue, state=HIDDEN)
		c.tongue_out=False

def cheeky(event):
	tongue_toggle()
	toggle_pupils()
	hide_happy(event)
	root.after(3000, tongue_toggle)	
	root.after(3000, toggle_pupils)
	return

def show_happy(event):
	if(20 <= event.x and event.x <= 350) and (20 <= event.y and event.y <= 350):
		c.itemconfigure(left_cheek, state=NORMAL)
		c.itemconfigure(right_cheek, state=NORMAL)
		c.itemconfigure(happy_mouth, state=NORMAL)
		c.itemconfigure(mouth_normal, state=HIDDEN)
		c.itemconfigure(sad_mouth, state=HIDDEN)
		c.happy_level= 10
	return


def hide_happy(event):
	c.itemconfigure(left_cheek, state=HIDDEN)
	c.itemconfigure(right_cheek, state=HIDDEN)
	c.itemconfigure(happy_mouth, state=HIDDEN)
	c.itemconfigure(mouth_normal, state=NORMAL)
	c.itemconfigure(sad_mouth, state=HIDDEN)
	return

def sad():
	if c.happy_level == 0:
		c.itemconfigure(happy_mouth, state= HIDDEN)
		c.itemconfigure(mouth_normal, state= HIDDEN)
		c.itemconfigure(sad_mouth, state= NORMAL)
		c.itemconfigure(main_tongue, fill="light green", outline= "light green")
		c.itemconfigure(tip_tongue, fill= "light green", outline= "light green")

	else:
		c.happy_level -= 1
	root.after(5000, sad)	

root = Tk()
c = Canvas (root , width=450, height=450)
c.configure(bg= 'dark green', highlightthickness=0)
c.body_color = "light green"


body = c.create_oval(35,20,365,350, outline= c.body_color, fill= c.body_color)


left_ear = c.create_polygon(75, 80, 75, 10, 165, 70, outline= c.body_color, fill= c.body_color)


right_ear= c.create_polygon(255,45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)


left_foot= c.create_oval(65,320,145,360, outline=c.body_color, fill=c.body_color)



right_foot= c.create_oval(250,320,330,360, outline= c.body_color, fill=c.body_color)


left_eye=c.create_oval(130,110,160,170, outline= "black", fill= "white")
left_pupil=c.create_oval(140, 145, 150, 155, outline="black", fill="black")


right_eye=c.create_oval(230,110, 260, 170, outline="black", fill="white")
right_pupil= c.create_oval(240,145, 250, 155, outline= "black", fill="black")

mouth_normal= c.create_line(170, 250, 200, 272,230, 250, smooth=1, width=1, state=NORMAL)


happy_mouth= c.create_line(170, 250, 200, 282,230, 250, smooth=1, width=2, state=HIDDEN)
sad_mouth=c.create_line(170, 250, 200, 232,230, 250, smooth=1, width=2, state=NORMAL)

main_tongue= c.create_rectangle(170, 250, 230, 290, outline= "red", fill= "red", state=HIDDEN)
tip_tongue= c.create_oval(170, 285, 230, 300, outline= "red", fill= "red", state=HIDDEN)

left_cheek = c.create_oval(70,180,120,230, outline="firebrick2", fill="firebrick2", state=HIDDEN)
right_cheek=c.create_oval(280,180,330,230, outline="firebrick2", fill="firebrick2", state=HIDDEN)


c.pack()
c.bind("<Motion>", show_happy)
c.bind("<Leave>", hide_happy)
c.bind("<Double-1>", cheeky)


c.happy_level= 10 
c.eyes_crossed= False
c.tongue_out=False
root.after(1000, blinking_pet)
root.after(5000, sad)

root.mainloop()