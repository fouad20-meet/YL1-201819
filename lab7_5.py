class Person():
   def __init__(self, name, fav_food ,age):
       self.name = name
       self.fav_food = fav_food
       self.age = age


   def define_color(self, color):
       self.color = color

   def print_info(self):
       print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
       print("My favorite food is " + self.fav_food + " and my favorite color is " + self.color)
a = Person("Britney", "Pizza", 16)
a.define_color("Black")
a.print_info()

b = Person("Jake","food", 15)
b.define_color("Black")
b.print_info()

