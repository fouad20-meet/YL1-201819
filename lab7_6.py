class Bear():
	def __init__(self, name):
		self.name = name
		print("A new bear created. Its name is: " + self.name)
	
	def say_hi(self):
		print("My name is " + self.name)
my_bear = Bear("Danny")
my_bear.say_hi()
