from turtle import *
import turtle
import random
colormode(255)
class Square(Turtle):
	def __init__(self, side):
		Turtle.__init__(self)
		self.side = side
		self.shape("square")
		self.shapesize(side*side)
	def random_color(self):
		self.color(random.randint(0,255),random.randint(0,255),random.randint(0,255)) 

		



square= Square(1)
square.random_color()

square.begin_poly()
square.fd(100)
square.right(60)
square.fd(100)
square.right(60)
square.fd(100)
square.right(60)
square.fd(100)
square.right(60)
square.fd(100)
square.right(60)
square.fd(100)
square.end_poly()

shape = square.get_poly()
register_shape("First Shape",shape)

class Hexagon():
	def __init__(self, arg):
		self.shape = ("First Shape")
		

turtle.mainloop()