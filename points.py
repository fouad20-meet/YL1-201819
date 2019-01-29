from turtle import *
class Points(Turtle):
	def __init__(self,x,y,r,color):
		Turtle.__init__(self)
		self.r = r
		self.shape("circle")
		self.color(color)
		self.pu()
		self.goto(x,y)
		self.shapesize(r/10)
		self.timer = 0
	def newPoint(self,x,y,r, color):
		self.r = r
		self.shape("circle")
		self.color(color)
		self.penup()
		self.goto(x,y)
		self.shapesize(r/10)
		self.timer = 100
