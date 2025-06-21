#Class with Default, One-Arg, and Two-Arg Constructors
class MyClass:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default Constructor Called")
        elif b is None:
            print("One-Arg Constructor Called with:", a)
        else:
            print("Two-Arg Constructor Called with:", a, b)

# Main class usage
print("Constructor Calls:")
obj1 = MyClass()
obj2 = MyClass(10)
obj3 = MyClass(10, 20)
#Call Superclass Constructors (Default & Argument) from Child Class
class SuperClass:
    def __init__(self, message="Default from Super"):
        print("SuperClass Constructor:", message)

class ChildClass(SuperClass):
    def __init__(self):
        super().__init__()  # Call default constructor
        print("ChildClass Constructor: Default")

class ChildWithArgs(SuperClass):
    def __init__(self):
        super().__init__("Called from Child with Arg")
        print("ChildWithArgs Constructor")

print("\nSuperclass Constructor Calls:")
c1 = ChildClass()
c2 = ChildWithArgs()
#Access Modifiers in Constructors (Python Style)
class AccessDemo:
    def __init__(self):
        print("Public Constructor")

    def _protected_constructor(self):
        print("Protected Constructor (Method-based simulation)")

    def __private_constructor(self):
        print("Private Constructor (Name mangling)")

    def call_all(self):
        self._protected_constructor()
        self.__private_constructor()

print("\nAccess Modifiers:")
obj = AccessDemo()
obj.call_all()
#Access Modifiers in Constructors 
class AccessDemo:
    def __init__(self):
        print("Public Constructor")

    def _protected_constructor(self):
        print("Protected Constructor (Method-based simulation)")

    def __private_constructor(self):
        print("Private Constructor (Name mangling)")

    def call_all(self):
        self._protected_constructor()
        self.__private_constructor()

print("\nAccess Modifiers:")
obj = AccessDemo()
obj.call_all()
#Attributes of a Constructor (Illustrate how constructor sets object state)
class Student:
    def __init__(self, name, age):
        self.name = name      # Attribute 1
        self.age = age        # Attribute 2

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

print("\nConstructor Attribute Example:")
student = Student("Alisha", 22)
student.display()

