
# Swap values using tuple unpacking
a, b = 5, 10
a, b = b, a
print("Swapped values:", a, b)

# Multiple assignments in a single line
x, y, z = 1, 2, 3
print("Multiple assignments:", x, y, z)

# List comprehension to create a list
squares = [x**2 for x in range(5)]
print("List comprehension:", squares)

# Enumerating over a list
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits):
    print(f"Index: {index}, Value: {value}")

# Using `zip` to iterate over multiple iterables
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")

# Unpacking with `*` and `**`
first, *rest = [1, 2, 3, 4, 5]
print("Unpacking with *:", first, rest)

# Concatenating strings using f-strings
greeting = "Hello"
name = "World"
message = f"{greeting}, {name}!"
print("Concatenated string:", message)

# Default dictionary values
from collections import defaultdict
my_dict = defaultdict(int)
my_dict['key'] += 1
print("Default dictionary values:", my_dict['key'])

# One-liner if-else statement
result = "Even" if 10 % 2 == 0 else "Odd"
print("One-liner if-else:", result)

# Unpacking in a function
def add(*args):
    return sum(args)

numbers = [1, 2, 3, 4, 5]
print("Unpacking in a function:", add(*numbers))

# List slicing with steps
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = numbers[::2]
print("List slicing with steps:", even_numbers)

# Using set to remove duplicates
duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(duplicates))
print("Removing duplicates with set:", unique_numbers)

# Reversing a list
reversed_list = numbers[::-1]
print("Reversing a list:", reversed_list)

# Dictionary unpacking
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print("Dictionary unpacking:", merged_dict)

# Using `any()` and `all()` functions
bool_list = [True, False, True]
any_result = any(bool_list)
all_result = all(bool_list)
print("Using any() and all():", any_result, all_result)
