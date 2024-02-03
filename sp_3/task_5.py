"""
Create decorator logger. The decorator should print to the console information about function's name and all its arguments separated with ',' for the function decorated with logger.

Create function concat with any numbers of any arguments which concatenates arguments and apply logger decorator for this function. 

For example

print(concat(2, 3)) display
Executing of function concat with arguments 2, 3...
23

print(concat('hello', 2)) display
Executing of function concat with arguments hello, 2...
hello2

print(concat (first = 'one', second = 'two')) display
Executing of function concat with arguments one, two...
onetwo
"""
def logger(func):
    def wrapper(*args, **kwargs):
        all_args = ", ".join(map(str, args + tuple(kwargs.values())))
        result = func(*args, **kwargs)
        print(f"Executing of function {func.__name__} with arguments {all_args}...")
        return result
    return wrapper

@logger
def concat(*args, **kwargs):
    args_generator = list((str(item) for item in args))
    kwargs_generator = list(str(item) for item in kwargs.values())
    if args and kwargs:
        return "".join(args_generator + kwargs_generator)
    if args:
        return "".join(args_generator)
    if kwargs:
        return "".join(kwargs_generator)

@logger
def sum(a,b):
    return a+b
    
@logger
def print_arg(arg):
    print(arg)
