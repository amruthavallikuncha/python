
# Initializing tuples
tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)

# Basic Tuple Operations
length_of_tuple_a = len(tuple_a)
element_at_index_two = tuple_a[2]
subset_of_tuple_a = tuple_a[1:4]

# Concatenating tuples
concatenated_tuples = tuple_a + tuple_b

# Repeating a tuple
repeated_tuple = tuple_a * 3

# Modifying tuples - not directly possible, so creating a new tuple
modified_tuple = tuple_a[:2] + (10, ) + tuple_a[3:]

# Unpacking tuples
first_element, *rest_of_elements, last_element = tuple_a

# Checking for membership
is_present_in_tuple_a = 2 in tuple_a

# Advanced Tuple Operations
# Tuple comprehension (technically, it's a generator expression)
squared_tuple = tuple(x**2 for x in tuple_a)

# Creating a named tuple
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age', 'city'])
person_info = Person('John', 30, 'New York')

# Accessing elements in a named tuple
person_name = person_info.name

# Converting a tuple to a list
tuple_to_list = list(tuple_a)

# Converting a list to a tuple
list_to_tuple = tuple(tuple_b)

# Using zip to create a tuple of pairs
zipped_tuple = tuple(zip(tuple_a, tuple_b))

# Counting occurrences of an element
count_of_five = tuple_a.count(5)

# Finding the index of an element
index_of_four = tuple_b.index(4)

# Using max and min with tuples
max_value = max(tuple_a)
min_value = min(tuple_b)

# Checking for equality of tuples
are_equal = tuple_a == tuple_b

# Iterating through a tuple
for element in tuple_a:
    print(element)

# Creating an empty tuple
empty_tuple = ()
