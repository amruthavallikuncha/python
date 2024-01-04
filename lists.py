
%%writefile /content/drive/MyDrive/Github_Handson/lists.py

# Initializing a list of numbers
numbers = [1, 2, 3, 4, 5]

# Basic List Operations
length_of_numbers = len(numbers)
element_at_index_two = numbers[2]
subset_of_numbers = numbers[1:4]
numbers[0] = 10
numbers.append(6)
numbers.remove(3)
is_present = 2 in numbers
index_of_four = numbers.index(4)
count_of_five = numbers.count(5)
reversed_numbers = list(reversed(numbers))
numbers.sort()
numbers_copy = numbers.copy()
numbers_copy.clear()

# Advanced List Operations
squared_numbers = [x**2 for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]
letters = ['a', 'b', 'c', 'd', 'e']
combined_list = list(zip(numbers, letters))
unpacked_numbers, unpacked_letters = zip(*combined_list)
squared_numbers_lambda = list(map(lambda x: x**2, numbers))
filtered_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))

# Generating a list using range
range_list = list(range(1, 11))
doubled_range = [x * 2 for x in range_list]

# Extending a list with another list
extension_list = [6, 7, 8]
numbers.extend(extension_list)

# Inserting an element at a specific index
numbers.insert(2, 11)

# Popping the last element from the list
popped_element = numbers.pop()

# Basic List Operations
numbers = [1, 2, 3, 4, 5]

# Length of the list
length_of_numbers = len(numbers)
print(f"Length of the list: {length_of_numbers}")

# Accessing elements in the list
first_element = numbers[0]
last_element = numbers[-1]
print(f"First element: {first_element}, Last element: {last_element}")

# Slicing the list
subset = numbers[1:4]
print(f"Subset of the list: {subset}")

# Adding elements to the list
numbers.append(6)
numbers.extend([7, 8])
print(f"List after adding elements: {numbers}")

# Removing elements from the list
removed_element = numbers.pop(2)
print(f"List after removing element at index 2: {numbers}, Removed element: {removed_element}")

# Checking if an element is in the list
is_present = 5 in numbers
print(f"Is 5 present in the list? {is_present}")

# Count occurrences of an element in the list
count_of_5 = numbers.count(5)
print(f"Count of 5 in the list: {count_of_5}")

# Finding the index of an element
index_of_4 = numbers.index(4)
print(f"Index of 4 in the list: {index_of_4}")

# Reversing the list
reversed_numbers = list(reversed(numbers))
print(f"Reversed list: {reversed_numbers}")

# Sorting the list
sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}")

# Advanced List Operations
# Using list comprehension to create a new list
squared_numbers = [x ** 2 for x in numbers]
print(f"Squared numbers: {squared_numbers}")

# Filtering elements using list comprehension
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Mapping a function to each element in the list
def add_one(x):
    return x + 1

modified_numbers = list(map(add_one, numbers))
print(f"List after adding 1 to each element: {modified_numbers}")

# Using lambda function in list comprehension
squared_numbers_lambda = [(lambda x: x ** 2)(x) for x in numbers]
print(f"Squared numbers using lambda function: {squared_numbers_lambda}")

# Combining two lists using zip
letters = ['a', 'b', 'c']
combined_list = list(zip(numbers, letters))
print(f"Combined list: {combined_list}")


%%writefile /content/drive/MyDrive/Github_Handson/lists.py

# Initializing a list of numbers
numbers = [1, 2, 3, 4, 5]

# Basic List Operations
length_of_numbers = len(numbers)
length_of_numbers

# Accessing elements by index
third_element = numbers[2]
third_element

# Slicing the list
subset_of_numbers = numbers[1:4]
subset_of_numbers

# Modifying elements in the list
numbers[0] = 10
numbers

# Appending an element to the end of the list
numbers.append(6)
numbers

# Removing an element by value
numbers.remove(3)
numbers

# Checking if an element is in the list
is_present = 2 in numbers
is_present

# Finding the index of an element
index_of_four = numbers.index(4)
index_of_four

# Counting occurrences of an element
count_of_five = numbers.count(5)
count_of_five

# Reversing the list
reversed_numbers = list(reversed(numbers))
reversed_numbers

# Sorting the list
numbers.sort()
numbers

# Creating a copy of the list
numbers_copy = numbers.copy()
numbers_copy

# Clearing all elements from the list
numbers_copy.clear()
numbers_copy

# Advanced List Operations
# Using list comprehension to create a new list
squared_numbers = [x**2 for x in numbers]
squared_numbers

# Filtering elements with list comprehension
even_numbers = [x for x in numbers if x % 2 == 0]
even_numbers

# Combining two lists using zip
letters = ['a', 'b', 'c', 'd', 'e']
combined_list = list(zip(numbers, letters))
combined_list

# Unpacking elements from a list of tuples
unpacked_numbers, unpacked_letters = zip(*combined_list)
unpacked_numbers, unpacked_letters

# Using lambda function with map to perform operation on each element
squared_numbers_lambda = list(map(lambda x: x**2, numbers))
squared_numbers_lambda

# Using filter with lambda function to filter elements
filtered_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
filtered_numbers_lambda
