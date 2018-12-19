# Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".

class Person:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
	def speak(self):
		print("My name is "+ self.first_name + " " + self.last_name)
me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.speak()
