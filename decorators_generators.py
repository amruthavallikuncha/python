
# Simple Function
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print("Result of adding numbers:", result)

# Decorators - Basic Example
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("John")

# Decorators - with Parameters
def greeting_decorator(greeting_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(greeting_message)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@greeting_decorator("Welcome to the program!")
def multiply_numbers(a, b):
    return a * b

result = multiply_numbers(3, 4)
print("Result of multiplying numbers:", result)

# Generators - Basic Example
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

for value in gen:
    print("Generated value:", value)

# Generators - Infinite Sequence
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# Using a generator in a for loop
for i in infinite_sequence():
    if i > 5:
        break
    print("Infinite sequence value:", i)

# Using the itertools module with a generator
from itertools import islice

limited_gen = islice(infinite_sequence(), 5)
print("Limited sequence values:", list(limited_gen))
