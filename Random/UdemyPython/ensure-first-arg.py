from functools import wraps

def ensure_first_arg_is(val):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			if args and args[0] != val:
				return f"First arg needs to be {val}"
			return fn(*args, **kwargs)
		return wrapper
	return inner


@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)

print(fav_foods("burrito", "ice cream")) # ('burrito', 'ice cream')
print(fav_foods("ice cream", "burrito")) # 'Invalid! First argument must be burrito'

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

print(add_to_ten(10, 12)) # 12
print(add_to_ten(1, 2)) # 'Invalid! First argument must be 10'
