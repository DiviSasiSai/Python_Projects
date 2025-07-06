print("Grocery List")
print("1.Add Item \n2.View Items \n3.Delete Item \n4.Exit")

grocery_list =[]

while True :
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            item = input("Enter item name: ")
            grocery_list.append(item)
        case 2:
            print(f"Grocery List: \n{grocery_list}")
        case 3:
            item = input("Enter item name: ")
            grocery_list.remove(item)
            print(f"The item {item} was removed.")
        case 4:
            print("You chose to exit,Thank You")
            break
        case _:
            print("Invalid Choice,Try again")
