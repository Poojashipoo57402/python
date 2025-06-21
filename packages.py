#create an abstract class with abstract and non-abstract
from abc import ABC, abstractmethod

class AbstractDemo(ABC):
    def non_abstract_method(self):
        print("This is a non-abstract method from the abstract class.")

    @abstractmethod
    def abstract_method(self):
        pass
#Create a subclass and access the non-abstract method using the abstract class object (from child)
class ChildDemo(AbstractDemo):
    def abstract_method(self):
        print("Abstract method implemented in child class.")

# Creating object of child class but referring to abstract class type
obj: AbstractDemo = ChildDemo()
obj.non_abstract_method()  # Accessing non-abstract method
# Create an instance of child class in child class and call abstract method
class ChildDemo2(AbstractDemo):
    def abstract_method(self):
        print("Abstract method implemented in ChildDemo2.")

    def call_abstract(self):
        print("Calling abstract method from inside the child class:")
        self.abstract_method()

obj2 = ChildDemo2()
obj2.call_abstract()
# Create an instance of child class in child class and call non-abstract method
class ChildDemo3(AbstractDemo):
    def abstract_method(self):
        print("Implemented abstract method in ChildDemo3.")

    def call_non_abstract(self):
        print("Calling non-abstract method from child class:")
        self.non_abstract_method()

obj3 = ChildDemo3()
obj3.call_non_abstract()




