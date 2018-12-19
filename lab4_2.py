class Rectangle(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def area(self):
		return self.width * self.height
	def perimeter(self):
		return (self.width + self.height)*2
	def print_prop(self):
		print(self.width)
		print(self.height)

rec1 = Rectangle(5,10)
print(rec1.area())
print(rec1.perimeter())
rec1.print_prop()