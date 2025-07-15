#  You are creating a fantasy video game. The data structure to model the
# player’s inventory will be a dictionary where the keys are string values
# describing the item in the inventory and the value is an integer value detail
# ing how many of that item the player has. For example, the dictionary value
# {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the
# player has 1 rope, 6 torches, 42 gold coins, and so on.

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(stuff):
    print("The inventory is :")
    totalItems = 0
    for key, value in stuff.items():
        print(f"{value} {key}")
        totalItems+=value
    print("Total number of items: ", totalItems)

def add_to_inventory(stuff,addinv):
    # inv = {}
    # for i in addinv:
    #     inv.setdefault(i,0)
    #     inv[i] +=1
    # for key,val in inv.items():
    #     stuff[key] +=val

    for i in addinv:
        stuff[i] = stuff.get(i,0) + 1
    display_inventory(stuff)

add_to_inventory(stuff,['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'])


