#Private Fields & Methods (with Subclass Attempt)
class MyClass:
    def __init__(self):
        self.__private_field = "I'm private"
    
    def __private_method(self):
        print("This is a private method")

    def main(self):
        print("Accessing private field in main method:", self.__private_field)
        self.__private_method()

class SubClass(MyClass):
    def access_private(self):
        try:
            print(self.__private_field)  # Will raise AttributeError
        except AttributeError:
            print("Cannot access private field from subclass")
        
        try:
            self.__private_method()  # Will raise AttributeError
        except AttributeError:
            print("Cannot access private method from subclass")

# Usage
obj = MyClass()
obj.main()

sub = SubClass()
sub.access_private()
#protected fields
class ProtectedClass:
    def __init__(self):
        self._protected_field = "I'm protected"

    def _protected_method(self):
        print("Protected method called")

class SamePackageClass:
    def demo(self):
        obj = ProtectedClass()
        print("Accessing:", obj._protected_field)
        obj._protected_method()


sp = SamePackageClass()
sp.demo()

#Public Fields and Methods
class PublicClass:
    def __init__(self):
        self.public_field = "I'm public"

    def public_method(self):
        print("Public method called")

# Accessible from anywhere
obj = PublicClass()
print(obj.public_field)
obj.public_method()


