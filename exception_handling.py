
# Simple try-except block
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Handling multiple exceptions
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Using else block in exception handling
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print(f"Entered number: {number}")

# Using finally block
try:
    file = open("nonexistent_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    if 'file' in locals() or 'file' in globals():
        file.close()

# Raising custom exceptions
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomError("This is a custom exception.")
except CustomError as e:
    print(f"Custom Exception: {e.message}")

# Assertion error
try:
    age = 15
    assert age >= 18, "You must be 18 or older."
except AssertionError as e:
    print(f"Assertion Error: {e}")

# Using except without an exception type
try:
    result = 10 / 0
except:
    print("An error occurred.")

# Handling exceptions in a loop
numbers = [1, 2, 3, 'four', 5]
for num in numbers:
    try:
        square = num ** 2
        print(f"The square of {num} is {square}")
    except TypeError:
        print(f"Error: {num} is not a valid number.")

# Using except with multiple exception types
try:
    value = int("abc")
except ValueError:
    print("ValueError occurred.")
except TypeError:
    print("TypeError occurred.")
except Exception as e:
    print(f"Other Exception: {e}")
