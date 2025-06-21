#Class with PRIVATE fields and methods
class PrivateDemo:
    def __init__(self):
        self.__private_field = "Private Field"

    def __private_method(self):
        print("Private Method Called")

    def main(self):
        print("Accessing in same class:", self.__private_field)
        self.__private_method()

# Subclass trying to access private members
class SubPrivateDemo(PrivateDemo):
    def try_access(self):
        try:
            print(self.__private_field)  # Will raise AttributeError
        except AttributeError:
            print("Cannot access private field in subclass")

        try:
            self.__private_method()  # Will raise AttributeError
        except AttributeError:
            print("Cannot access private method in subclass")


print("PRIVATE ACCESS TEST")
private_obj = PrivateDemo()
private_obj.main()

sub_obj = SubPrivateDemo()
sub_obj.try_access()
# Class with PROTECTED fields and methods
# Simulate same-package access
class ProtectedDemo:
    def __init__(self):
        self._protected_field = "Protected Field"

    def _protected_method(self):
        print("Protected Method Called")

# Access from same package
class SamePackageAccess:
    def access_protected(self):
        obj = ProtectedDemo()
        print("Same package accessing:", obj._protected_field)
        obj._protected_method()

# Subclass from a different "package"
class SubProtectedDemo(ProtectedDemo):
    def access_from_subclass(self):
        print("Subclass accessing:", self._protected_field)
        self._protected_method()

# Access from another class in "different package"
def external_access():
    obj = ProtectedDemo()
    print("External access to protected:", obj._protected_field)
    obj._protected_method()

print("\nPROTECTED ACCESS TEST")
SamePackageAccess().access_protected()
SubProtectedDemo().access_from_subclass()
external_access()
## Simulate same-package access
class ProtectedDemo:
    def __init__(self):
        self._protected_field = "Protected Field"

    def _protected_method(self):
        print("Protected Method Called")

# Access from same package
class SamePackageAccess:
    def access_protected(self):
        obj = ProtectedDemo()
        print("Same package accessing:", obj._protected_field)
        obj._protected_method()

# Subclass from a different "package"
class SubProtectedDemo(ProtectedDemo):
    def access_from_subclass(self):
        print("Subclass accessing:", self._protected_field)
        self._protected_method()

# Access from another class in "different package"
def external_access():
    obj = ProtectedDemo()
    print("External access to protected:", obj._protected_field)
    obj._protected_method()

print("\nPROTECTED ACCESS TEST")
SamePackageAccess().access_protected()
SubProtectedDemo().access_from_subclass()
external_access()
# Class with PROTECTED fields and methods
# Simulate same-package access
class ProtectedDemo:
    def __init__(self):
        self._protected_field = "Protected Field"

    def _protected_method(self):
        print("Protected Method Called")

# Access from same package
class SamePackageAccess:
    def access_protected(self):
        obj = ProtectedDemo()
        print("Same package accessing:", obj._protected_field)
        obj._protected_method()

# Subclass from a different "package"
class SubProtectedDemo(ProtectedDemo):
    def access_from_subclass(self):
        print("Subclass accessing:", self._protected_field)
        self._protected_method()

# Access from another class in "different package"
def external_access():
    obj = ProtectedDemo()
    print("External access to protected:", obj._protected_field)
    obj._protected_method()

print("\nPROTECTED ACCESS TEST")
SamePackageAccess().access_protected()
SubProtectedDemo().access_from_subclass()
external_access()
# Class with PUBLIC fields and methods
class PublicDemo:
    def __init__(self):
        self.public_field = "Public Field"

    def public_method(self):
        print("Public Method Called")

# Access from anywhere
def public_access():
    obj = PublicDemo()
    print("Accessing public field:", obj.public_field)
    obj.public_method()

print("\nPUBLIC ACCESS TEST")
public_access()
#