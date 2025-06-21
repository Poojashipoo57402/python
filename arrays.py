#Add integer values of an array

def sum_array(arr):
    return sum(arr)
 # Calculate average value of an array of integers
def average_array(arr):
    return sum(arr) / len(arr) if arr else 0
#Find index of an array element
a=[1,2,3]
print(a[0])
#Test if array contains a specific value
a=[1,2,3]
for i in a:
    print(i)

# Remove a specific element from an array
a=[1,2,3]
print(a.pop(1))
#Copy an array to another array
a=[1,2,3]
b=[]
b=a.copy()
print(b)

#Insert an element at a specific position in the array
a=[1,2,3]
a.insert(0,2)
print(a)
#Find the minimum and maximum value of an array
a=[1,2,3]
print(max(a))
print(min(a))

#Reverse an array of integer values
a=[1,2,3]
a.reverse()
print(a)
#Find the duplicate values of an array

def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for x in arr:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)

    return list(duplicates)

arr = [1, 2, 3, 2, 4, 5, 6, 4, 4]
print("Duplicates:", find_duplicates(arr))

#Find the common values between two arrays

def find_common(arr1, arr2):
    return list(set(arr1) & set(arr2))
#Remove duplicate elements from an array

def remove_duplicates(arr):
    return list(dict.fromkeys(arr))
#Find the second largest number in an array

def second_largest(arr):
    unique = list(set(arr))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

#Count even and odd numbers in an array

def count_even_odd(arr):
    even = sum(1 for x in arr if x % 2 == 0)
    odd = len(arr) - even
    return even, odd
#Get the difference of largest and smallest value

def diff_max_min(arr):
    return max(arr) - min(arr)
#Verify if array contains two specified elements (12, 23)

def contains_12_23(arr):
    # Check if both 12 and 23 are present in the array
    return 12 in arr and 23 in arr


arr1 = [10, 12, 15, 23, 45]
arr2 = [1, 2, 3, 12]

print("Array 1 contains 12 and 23?", contains_12_23(arr1))  # True
print("Array 2 contains 12 and 23?", contains_12_23(arr2))

#Remove duplicate elements and return the new array
def remove_duplicates(arr):
    return list(dict.fromkeys(arr))


original_array = [1, 2, 2, 3, 4, 4, 5]
new_array = remove_duplicates(original_array)

print("Original Array:", original_array)
print("Array after removing duplicates:", new_array)











