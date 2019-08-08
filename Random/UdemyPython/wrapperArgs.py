# NOT WORKING CODE!
# JUST FOR DEMO PURPOSES!

# When we write:
@decorator
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator(func)


# When we write:
@decorator_with_args(arg)
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator_with_args(arg)(func)
