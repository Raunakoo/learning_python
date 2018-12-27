class things:
	pass
class inanimate(things):	
	pass
class animate(things):
	pass
class sidewalks(inanimate):
	pass		
class animals(animate):
	def breathe(self):
		print('i am breathing')
	def move(self):
		print('moving')

	def eat(self):
		print('eating a lot')
	                  							
class mammals(animals):
	def feedmilk(self):
		print('feeding babies')
		pass

class giraffes():
	def dance(self):
		print('left foot forward\
              left foot back\
              right foot forward\
              right foot back\
              left foot back')

	def __init__(self, spots):
		self.giraffe_spots = spots

	def Harold(self):
		print('i am Harold,')

	def Reginald(self):
		print('i am Reginald,')

	def find_food(self):
		self.move()
		print('i\'ve found food!hooray' )
		self.eat()

	def dance_a_jig(self):
		self.move()
		self.move()	  			
		self.move()
		self.move()
		self.move()
		self.move()
	def eat_leaf(self):
		print('eating leaves!yummy!')

	def breathe(self):
		print('i am breathing')

	def move(self):
		print('moving')

	def eat(self):
		print('eating a lot')

	def feedmilk(self):
		print('feeding babies')

		pass
Reginald=giraffes(100)
Reginald.dance()	

'''print('giraffe function executed')
'''#pass
#Reginald=giraffes()

'''Reginald.Reginald()
Reginald.breathe()
Reginald.move()
Reginald.dance_a_jig()
Reginald.feedmilk()
Reginald.eat_leaf()

#Harold's code
Harold=giraffes()
Harold.Harold()
Harold.move()
Harold.eat_leaf()'''



'''Jasmeen=turtle.Pen()
Mandeep=turtle.Pen()
#jasmeen's code
Jasmeen.forward(50)
Jasmeen.right(90)
Jasmeen.forward(20)


#mandeep's code
Mandeep.left(90)
Mandeep.forward(100)'''

#raunak's code
'''raunak=turtle.Pen()
raunak.left(180)
raunak.forward(80)'''

#raunak2's code
'''raunak=turtle.Pen()
raunak.right(30)'''
turtle.done()

nanupapa=giraffes(100)
nanimama=giraffes(150)
print(nanupapa.giraffe_spots)
print(nanimama.giraffe_spots)

class cool_class_function:
	def cool():
		print('class_function')

	def cool2():
		print('class_function2')			