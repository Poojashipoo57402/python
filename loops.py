#Print “Bright IT Career” 10 times using for loop
for i in range(10):
    print("Bright IT Career")
#Print 1 to 20 using while loop
i =1
while i<=20:
    print(i)
    i+=1
#Equal and Not Equal Operators
a = 101
b = 200

print("a == b:", a == b)
print("a != b:", a != b)
#Print Odd and Even Numbers (1–20)
for i in range(1, 21):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

#largest of 3 number
def largest_of_three(a, b, c):
    largest = max(a, b, c)
    print("Largest number is:", largest)

largest_of_three(10, 25, 15)
# Print Even Numbers Between 10 and 20 using while loop
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
#do while loop
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break
#armstrong num
def is_armstrong(num):
    sum = 0
    temp = num
    n = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    return sum == num

print("Is 153 Armstrong?", is_armstrong(153))
print("Is 123 Armstrong?", is_armstrong(123))
#prime number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7))
print("Is 9 prime?", is_prime(9))
#palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

print("Is 121 palindrome?", is_palindrome(121))
print("Is 123 palindrome?", is_palindrome(123))
#Check Even or Odd using switch (Python 3.10+)

def check_even_odd(n):
    match n % 2:
        case 0:
            print("Even")
        case 1:
            print("Odd")

check_even_odd(4)
check_even_odd(7)

#gendercheck
def print_gender(gender):
    match gender.upper():
        case 'M':
            print("Male")
        case 'F':
            print("Female")
        case _:
            print("Invalid input")

print_gender('M')
print_gender('F')
print_gender('X')