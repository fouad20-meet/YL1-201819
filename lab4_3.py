class Person(object):
	def __init__(self, name, age, city, gender, weight):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.weight = weight
	def eat_favorite_breakfast(self):
		return self.weight+5
	def play_favorite sport(self):
		return self.weight-5
p1 = Person(noy, 15, Kfar, Female, 500)