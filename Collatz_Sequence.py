#  Write a function named collatz() that has one parameter named number. If
# number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.
#  Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1.

"""
#Using Loops
def collatz_sequence(number):
    if number % 2 ==0:
        print(f"{number // 2}")
        return number // 2
    else:
        print(f"{3* number + 1}")
        return 3 * number + 1

number = int(input("Enter a number: "))

while number != 1:
    number = collatz_sequence(number)
"""

#Recursion
def collatz_sequence(number):
    if number == 1:
        print(f"{1}")
        return
    if number % 2 ==0:
        print(f"{number // 2}")
        collatz_sequence(number // 2)
        return
    else:
        print(f"{3* number + 1}")
        collatz_sequence(3 * number + 1)
        return

number = int(input("Enter a number: "))
collatz_sequence(number)