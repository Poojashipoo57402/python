#Generate ArithmeticException without exception handling

# This will raise ZeroDivisionError
print("Result:", 10 / 0)
#Handle ArithmeticException using try-except

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Arithmetic Exception: Division by zero is not allowed.")
    #Method That Throws Exception and Called Without Try Block

def raise_exception():
    raise ZeroDivisionError("Division error raised")

# No try block here
raise_exception()
# Program with Multiple except Blocks

try:
    a = int("hello")
except ValueError:
    print("Caught ValueError!")
except ZeroDivisionError:
    print("Caught ZeroDivisionError!")
#Throw Exception with Custom Message

def throw_custom_exception():
    raise Exception("This is a custom exception message.")

try:
    throw_custom_exception()
except Exception as e:
    print("Caught:", e)
#Create Your Own Exception

class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("This is my custom exception.")
except MyCustomError as e:
    print("Caught:", e)
#Program with finally Block

try:
    x = 10 / 2
    print("Result:", x)
finally:
    print("This will always execute (finally block).")
#Generate ArithmeticException (Python: ZeroDivisionError)

a = 1 / 0  # Raises ZeroDivisionError
#Generate FileNotFoundException

try:
    with open("nonexistent.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("Caught: FileNotFoundError")
