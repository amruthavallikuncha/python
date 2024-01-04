
# Initializing dictionaries
student = {"name": "John", "age": 20, "grade": "A"}
scores = {"math": 90, "science": 85, "history": 92}

# Basic Dictionary Operations
length_of_student_dict = len(student)
value_of_age = student["age"]
student["grade"] = "B"
is_name_present = "name" in student
keys_in_student = student.keys()
values_in_student = student.values()
items_in_student = student.items()

# Adding a new key-value pair
student["gender"] = "Male"

# Removing a key-value pair
removed_score = scores.pop("science", None)

# Getting value with default if key not present
physics_score = scores.get("physics", None)

# Advanced Dictionary Operations
# Dictionary comprehension to create a new dictionary
squared_scores = {subject: score**2 for subject, score in scores.items()}

# Merging dictionaries using update method
additional_scores = {"chemistry": 88, "biology": 94}
scores.update(additional_scores)

# Copying a dictionary
scores_copy = scores.copy()

# Clearing all elements from a dictionary
scores_copy.clear()

# Nested dictionaries
students = {
    "John": {"age": 20, "grade": "A"},
    "Alice": {"age": 22, "grade": "B"},
    "Bob": {"age": 21, "grade": "C"}
}

# Accessing nested dictionary values
johns_age = students["John"]["age"]

# Using setdefault to add a key with default value if not present
default_value = scores.setdefault("english", 80)

# Popitem to remove and return an arbitrary key-value pair
removed_item = scores.popitem()

# Creating a dictionary with default values using defaultdict
from collections import defaultdict
default_dict = defaultdict(int)
default_dict["math"] += 1

# Using fromkeys to create a dictionary with default values
subjects = ["math", "science", "history"]
default_scores = dict.fromkeys(subjects, 0)

# Merging dictionaries using unpacking (**)
merged_dict = {**scores, **additional_scores}

# Using keys to get a view of dictionary keys
score_keys = scores.keys()

# Using values to get a view of dictionary values
score_values = scores.values()

# Using items to get a view of dictionary key-value pairs
score_items = scores.items()

# Iterating through keys in a dictionary
for key in scores:
    print(key)

# Iterating through items in a dictionary
for subject, score in scores.items():
    print(f"{subject}: {score}")
