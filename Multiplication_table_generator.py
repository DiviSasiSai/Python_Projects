number = int(input("Enter your number: "))
print(f"Multiplication Table of {number}:")

for i in range(1,11):
    print(f"{i} X {number} = {i*number}")