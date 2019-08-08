from random import choice
# We can nest functions inside one another
def greet(person):
	def get_mood():
		msg = choice(('Hello there ', 'Go away ', 'I love you '))
		return msg

	result = get_mood() + person
	return result

print(greet("Toby"))