from turtle import *
import random

class Ball(turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
	


b1 = Ball(10)
b2 = Ball(15)

def check_collision(ball1,ball2):
	D = math.sqrt(math.pow((ball2.xcor()-ball1.xcor()),2) + math.pow((ball2.ycor()-ball1.ycor()),2))
	if(D <= ball1.radius + ball2.radius):
		ball1.color("red")
		ball2.color("green")
