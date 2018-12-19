class Cat():
	def __init__(self, name):
		self.name = name
		self.age = 0 
	def birthday(self):
		self.age += 1
		if self.age >= 100:
			print("Dong dong, the cat is dead!")
		else:
			print(self.name + " having its " + str(self.age) + " birthday!")

my_cat = Cat("Salem")
my_cat.birthday()
# what I want: my cat to celebrate its 8th birthday (and all the 
# birthdays that come before that)
