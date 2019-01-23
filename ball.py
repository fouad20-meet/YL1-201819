from turtle import *
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shape("circle")
		self.color(color)
		self.penup()
		self.goto(x,y)
		self.shapesize(r/10)
	def move(self,screen_width,screen_height):
		current_x = self.xcor()
		new_x = self.dx + current_x
		current_y = self.ycor()
		new_y = self.dy + current_y
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		upper_side_ball = new_y + self.r
		lower_side_ball = new_y -self.r
		self.goto(new_x,new_y)
		if(right_side_ball >= screen_width):
			self.dx = -self.dx
		if(left_side_ball <= -screen_width):
			self.dx = -self.dx
		if(upper_side_ball >= screen_height):
			self.dy = -self.dy
		if(lower_side_ball <= -screen_height):
			self.dy = -self.dy
	def new_ball(self,x,y,dx,dy,r,color):
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shape("circle")
		self.color(color)
		self.penup()
		self.goto(x,y)
		self.shapesize(r/10)




