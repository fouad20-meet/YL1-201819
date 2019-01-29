import turtle
import time
import random
import math
from turtle import *
from ball import Ball
from points import Points

turtle.colormode(1)
turtle.bgpic("black.gif")
turtle.tracer(0,2)
turtle.hideturtle()

running = True
pause = False
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

my_ball = Ball(0,0,0,0,70,(random.random(), random.random(), random.random()))

number_of_balls = 5
minimum_ball_radius = 20
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5
number_of_points = 20

POINTS =[]

for i in range(-screen_width,screen_width,200):

	for j in range(-screen_height,screen_height,200):
		x = i
		y = j
		color = (random.random(), random.random(), random.random())
		Points1 = Points(x,y,10,color)
		POINTS.append(Points1)

BALLS = []

for i in range(number_of_balls):
	x = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
	y = random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
	dx = random.randint(minimum_ball_dx,maximum_ball_dx)
	while(dx == 0):
		dx = random.randint(minimum_ball_dx,maximum_ball_dx)
	dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	while(dy == 0):
		dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	print(dx,dy)
	r = random.randint(minimum_ball_radius,maximum_ball_radius)
	color = (random.random(), random.random(), random.random())
	Ball1 = Ball(x,y,dx,dy,r,color)
	BALLS.append(Ball1)

def move_all_balls():
	for i in BALLS:
		i.move(screen_width,screen_height)



def collide(ball_a,ball_b):
	if(ball_a == ball_b):
		return False
	# d = ((ball_a.xcor()-ball_b.xcor())**2 + (ball_a.ycor()-ball_b.ycor())**2)**0.
	d = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
	r1 = ball_a.r
	r2 = ball_b.r
	if (d < (r1+r2)-5):
		return True
	return False

def check_points_collision():
	all_balls = []
	all_balls.append(my_ball)
	for ball in BALLS:
		all_balls.append(ball)
	all_points = []
	for point in POINTS:
		all_points.append(point)
	for ball in all_balls:
		for point in all_points:
			if(collide(ball,point) and point.timer<=0):
				r = point.r
				x = point.xcor()
				y = point.ycor()
				color = (random.random(), random.random(), random.random())
				ball.r = ball.r + 2
				ball.shapesize(ball.r/10)
				point.newPoint(x,y,r,color)
				point.hideturtle()

def check_all_balls_collision():
	global running
	DX = 0 
	DY = 0
	all_balls=[]
	all_balls.append(my_ball)
	for ball in BALLS:
		all_balls.append(ball)
	for ball_a in all_balls:
		for ball_b in all_balls:
			if(collide(ball_a,ball_b)):
				r1 = ball_a.r
				r2 = ball_b.r
				X = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
				Y = random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
				while(DX == 0):
					DX = random.randint(minimum_ball_dx,maximum_ball_dx)
				while(DY == 0):
					DY = random.randint(minimum_ball_dy,maximum_ball_dy)
				R = random.randint(minimum_ball_radius,maximum_ball_radius)
				Color = (random.random(), random.random(), random.random())
				if(r1>r2):

					if(ball_b == my_ball):
						turtle.pencolor("red")
						turtle.goto(0,0)
						turtle.write("GAME OVER!", move=False, align="center", font=("Arial",64, "normal"))
						turtle.pencolor("black")
						time.sleep(1)
						running = False
					else:
						ball_b.new_ball(X,Y,DX,DY,R,Color)
					ball_a.r = r1 + 3
					ball_a.shapesize(ball_a.r/10)
				else:
					if(ball_a == my_ball):
						turtle.pencolor("red")
						turtle.goto(0,0)
						turtle.write("GAME OVER!", move=False, align="center", font=("Arial",64, "normal"))
						turtle.pencolor("black")
						time.sleep(1)
						running = False
					else:
						ball_a.new_ball(X,Y,DX,DY,R,Color)
					ball_b.r = r2 + 3
					ball_b.shapesize(ball_b.r/10)

def win():
	if(my_ball.shapesize()[1] >= 80):
		turtle.pu()
		turtle.goto(0,0)
		turtle.pencolor("yellow")
		turtle.write("YOU WIN!", move=False, align="center", font=("Arial",64, "normal"))
		turtle.pencolor("black")
		time.sleep(5)
		running = False


def movearound():
	my_ball.goto(turtle.getcanvas().winfo_pointerx()-screen_width*2,1.4*screen_height-turtle.getcanvas().winfo_pointery())

running = True

def spacebar():
	global pause
	print("space")
	if pause==False:
		pause=True
	else:
		pause = False

turtle.onkey(spacebar, "space") 
turtle.listen()



while running:
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2
	if not pause:
	    movearound()
	    move_all_balls()
	    check_points_collision()
	check_all_balls_collision()
	win()
	turtle.update()
	time.sleep(0.05)
	for point in POINTS:
		point.timer = point.timer-5
		if point.timer <= 0:
			point.showturtle()
	#print('here')


#turtle.bye()
# turtle.update()
turtle.mainloop()