#Define a static variable and access it through a class

class MyClass:
    static_var = 10  # Static variable

# Access through class
print("Accessed through class:", MyClass.static_var)
#Define a static variable and access it through an instance
class MyClass:
    static_var = 10

obj = MyClass()
print("Accessed through instance:", obj.static_var)
#Define a static variable and change it within an instance
class MyClass:
    static_var = 10

obj1 = MyClass()
obj2 = MyClass()

obj1.static_var = 20  # This creates a new instance variable, doesn't affect the class variable

print("obj1 static_var:", obj1.static_var)  # 20 (instance-level)
print("obj2 static_var:", obj2.static_var)  # 10 (still class-level)
print("Class static_var:", MyClass.static_var)  # 10
# Define a static variable and change it within the class
class MyClass:
    static_var = 10

    @classmethod
    def change_static_var(cls, value):
        cls.static_var = value

# Modify using class method
MyClass.change_static_var(50)

print("Class static_var:", MyClass.static_var)  # 50

# All instances reflect the change
obj = MyClass()
print("Accessed through instance:", obj.static_var)  # 50
