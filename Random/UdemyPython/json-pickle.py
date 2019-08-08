import jsonpickle

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

c = Cat("Charles", "Tabby")

# To JSONPICKLE 'c' the cat:
with open("cat.json", "w") as file:
	frozen = jsonpickle.encode(c)
	file.write(frozen)

# To bring back 'c' the cat using JSONPICKLE
# with open("cat.json", "r") as file:
# 	contents = file.read()
# 	unfrozen = jsonpickle.decode(contents)
# 	print(unfrozen)