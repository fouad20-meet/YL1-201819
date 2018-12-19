class Cake():
	def __init__(self,flavor):
		self.flavor = flavor

	def eat(self):
		print("Yummy!!! Eating a " + self.flavor + " cake :)")

cake = Cake("chocolate")
cake.eat()
# what I want to be printed: Yummy!!! Eating a chocolate cake :)


