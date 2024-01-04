
# Initializing sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Basic Set Operations
length_of_set_a = len(set_a)
is_present_in_set_a = 2 in set_a
union_of_sets = set_a | set_b
intersection_of_sets = set_a & set_b
difference_of_sets = set_a - set_b
symmetric_difference = set_a ^ set_b

# Modifying sets
set_a.add(6)
set_a.remove(3) if 3 in set_a else None
set_a.discard(4)
popped_element = set_a.pop() if set_a else None

# Advanced Set Operations
# Set comprehension to create a new set
squared_set = {x**2 for x in set_a}

# Checking for subset and superset
is_subset = {1, 2}.issubset(set_a)
is_superset = set_a.issuperset({1, 2})

# Copying a set
set_copy = set_a.copy()

# Clearing all elements from a set
set_copy.clear()

# Adding multiple elements to a set
set_a.update({7, 8, 9})

# Removing elements using discard for non-existing element
set_a.discard(10)

# Removing elements using difference_update
set_a.difference_update({5, 6})

# Using frozenset for an immutable set
frozen_set = frozenset(set_a)

# Converting a list to a set
list_to_set = set([2, 4, 6, 8, 10])

# Converting a set to a list
set_to_list = list(set_a)

# Using set operations with other data types
numeric_set = {1, 2, 3, 4, 5}
string_set = {'apple', 'orange', 'banana'}

# Combining sets with update method
numeric_set.update(string_set)

# Using intersection_update method
numeric_set.intersection_update({2, 4, 6})

# Checking for disjoint sets
are_disjoint = numeric_set.isdisjoint(string_set)

# Using symmetric_difference_update
numeric_set.symmetric_difference_update({1, 3, 5})

# Checking for equality of sets
are_equal = numeric_set == {1, 2, 3, 4, 5}

# Iterating through a set
for element in numeric_set:
    print(element)
