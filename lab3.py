import turtle
image = "giphy.gif"
turtle.addshape(image)
turtle.shape(image)
turtle.speed(0)
colors=["red","green","orange","yellow","blue","purple"]
for i in range(360):
	turtle.pencolor(colors[i%6])
	turtle.right(i)
	turtle.fd(300)
	turtle.right(60)
	turtle.fd(150)
	turtle.right(90)
	turtle.fd(75)
	turtle.home()
	
turtle.mainloop()