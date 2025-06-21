#arithmatic operators
def arithmetic_operations(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b if b != 0 else "Cannot divide by zero")
arithmetic_operations(10, 5)
def increment_decrement():
    x = 5
    print("Original:", x)
    x += 1  # Increment
    print("After Increment:", x)
    x -= 1  # Decrement
    print("After Decrement:", x)
increment_decrement()
#program for relational operators
def check_equality(a,b):
    if a==b:
        print("a is equal to b")
    else:
        print("a is  not equal to b")
check_equality(10,5)
#Print the Smaller and Larger Number
def min_max(a, b):
    print(min(a, b))
    print(max(a, b))
min_max(45, 30)