
class Hexagon(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
		for i in range (6):
			self.begin_poly()
			self.fd(100)
			self.right(60)
			self.end_poly()
		p = get_poly()
		register_shape("Hexagon", p)
turtle.mainloop()
		


