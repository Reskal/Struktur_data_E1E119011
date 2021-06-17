''' R-2.4 Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type. '''

class Flower:
	def __init__(self, name, petals, price):
		self._name = name
		self._petals = petals
		self._price = price

	def get_name(self):
		return self._name

	def get_petals(self):
		return self._petals

	def get_price(self):
		return self._price

	def set_name(self, name):
		self._name = name

	def set_petals(self, petals):
		self._petals = petals

	def set_price(self, price):
		self._price = price

# f = Flower('sunflower', 24, 1.25)
# print(f.get_name())
# print(f.get_petals())
# print(f.get_price())
# f.set_name('rose')
# f.set_petals(32)
# f.set_price(1.45)
# print(f.get_name())
# print(f.get_petals())
# print(f.get_price())
