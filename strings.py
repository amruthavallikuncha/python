
import re

# Initializing a string variable with your name
name = "Amruthavalli Kuncha"

# Basic String Operations
length_of_name = len(name)
print(f"Length of the name: {length_of_name}")

lowercase_name = name.lower()
print(f"Lowercase name: {lowercase_name}")

uppercase_name = name.upper()
print(f"Uppercase name: {uppercase_name}")

char_count = name.count('a')
print(f"Count of 'a' in the name: {char_count}")

starts_with_amrutha = name.startswith("Amrutha")
print(f"Does the name start with 'Amrutha'? {starts_with_amrutha}")

replaced_name = name.replace("Kuncha", "Smith")
print(f"Name after replacing 'Kuncha' with 'Smith': {replaced_name}")

name_parts = name.split(" ")
print(f"Name split into parts: {name_parts}")

greeting = "Hello, "
full_greeting = greeting + name
print(f"Full Greeting: {full_greeting}")

formatted_greeting = f"Hi, {name}! How are you doing today?"
print(formatted_greeting)

substring = name[4:14]
print(f"Substring from index 4 to 14: {substring}")

# Advanced String Operations
# Find the index of a substring
index_of_valli = name.find("Valli")
print(f"Index of 'Valli' in the name: {index_of_valli}")

# Check if the string contains only alphabetic characters
is_alpha = name.isalpha()
print(f"Is the name composed only of alphabetic characters? {is_alpha}")

# Check if the string contains only digits
contains_only_digits = name.isdigit()
print(f"Does the name contain only digits? {contains_only_digits}")

# Check if the string is titlecased
is_titlecased = name.istitle()
print(f"Is the name titlecased? {is_titlecased}")

# Strip leading and trailing whitespaces
trimmed_name = name.strip()
print(f"Name after stripping leading and trailing whitespaces: {trimmed_name}")

# Regex Patterns and Methods
# Using regex to find all occurrences of vowels
vowels = re.findall(r'[aeiou]', name, re.IGNORECASE)
print(f"All vowels in the name: {vowels}")

#  Using regex to find all words in the name
words = re.findall(r'\b\w+\b', name)
print(f"All words in the name: {words}")

# Using regex to replace digits with 'X'
name_with_digits = "Amrutha123Kuncha456"
name_without_digits = re.sub(r'\d', '', name_with_digits)
print(f"Name with digits removed: {name_without_digits}")
