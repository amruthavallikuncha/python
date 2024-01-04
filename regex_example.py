
import re

# Basic Regex - Matching
text = "Hello, my email is john@example.com"
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

match = re.search(pattern, text)
if match:
    print("Found email:", match.group())

# Regex - Groups and Capturing
date_text = "Today is 2023-01-15"
date_pattern = r'(\d{4})-(\d{2})-(\d{2})'

date_match = re.search(date_pattern, date_text)
if date_match:
    year, month, day = date_match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")

# Regex - Findall
text_with_numbers = "The prices are $10, $20, and $30"
number_pattern = r'\$\d+'

numbers_found = re.findall(number_pattern, text_with_numbers)
print("Found numbers:", numbers_found)

# Regex - Substitution
text_to_replace = "Replace stars with hearts: * * *"
substitute_pattern = r'\*'
substituted_text = re.sub(substitute_pattern, '❤️', text_to_replace)
print("Substituted text:", substituted_text)

# Regex - Flags
case_sensitive_text = "Python is awesome, python is easy"
case_sensitive_pattern = r'python'
case_sensitive_matches = re.findall(case_sensitive_pattern, case_sensitive_text)
print("Case-sensitive matches:", case_sensitive_matches)

case_insensitive_matches = re.findall(case_sensitive_pattern, case_sensitive_text, flags=re.IGNORECASE)
print("Case-insensitive matches:", case_insensitive_matches)

# Regex - Named Groups
phone_number_text = "Contact me at 123-456-7890"
phone_number_pattern = r'(?P<area>\d{3})-(?P<first>\d{3})-(?P<last>\d{4})'

phone_number_match = re.search(phone_number_pattern, phone_number_text)
if phone_number_match:
    print("Area Code:", phone_number_match.group('area'))
    print("First Part:", phone_number_match.group('first'))
    print("Last Part:", phone_number_match.group('last'))
