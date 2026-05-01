
# Read the inventory from the file

inventory = {}
with open("E:\Project\inventory.txt", "r") as f:
        for line in f:
            fields = line.strip().split(",")
            inventory[fields[0]] = int(fields[1]), float(fields[2])

# Function to write the inventory to the file
def write_inventory():
    with open("E:\Project\inventory.txt", "w") as f:
        for item in inventory:
            f.write(f"{item},{inventory[item][0]},{inventory[item][1]}\n")

# Function to add a new item to the inventory
def add_item():
    item_name = input("Enter the name of the item: ")
    if item_name in inventory:
        print("Item already exists in inventory")
        return
    item_price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity of the item: "))
    inventory[item_name] = quantity, item_price
    write_inventory()
    print(f"{item_name} has been added to the inventory")

# Function to remove an item from the inventory
def remove_item():
    item_name = input("Enter the name of the item: ")
    if item_name not in inventory:
        print("Item does not exist in inventory")
        return
    del inventory[item_name]
    write_inventory()
    print(f"{item_name} has been removed from the inventory")
# Function to add quantity of an item to the inventory
def add_quantity():
    item_name = input("Enter the name of the item: ")
    if item_name not in inventory:
        print("Item does not exist in inventory")
        return
    quantity = int(input("Enter the quantity to be added: "))
    current_quantity = inventory[item_name][0]
    new_quantity = current_quantity + quantity
    inventory[item_name] = (new_quantity, inventory[item_name][1])
    write_inventory()
    print(f"{quantity} {item_name} has been added to the inventory")

# Function to remove quantity of an item from the inventory
def remove_quantity():
    item_name = input("Enter the name of the item: ")
    if item_name not in inventory:
        print("Item does not exist in inventory")
        return
    quantity = int(input("Enter the quantity to be removed: "))
    current_quantity = inventory[item_name][0]
    if quantity > current_quantity:
        print(f"Only {current_quantity} {item_name} available")
        return
    new_quantity = current_quantity - quantity
    inventory[item_name] = (new_quantity, inventory[item_name][1])
    write_inventory()
    print(f"{quantity} {item_name} has been removed from the inventory")
# Function to change or update the price of an item
def update_price():
    item_name = input("Enter the name of the item: ")
    if item_name not in inventory:
        print("Item does not exist in inventory")
        return
    item_price = float(input("Enter the new price of the item: "))
    inventory[item_name] = (inventory[item_name][0], item_price)
    
    write_inventory()  # update text file
    print(f"The price of {item_name} has been changed to {item_price}")

# Function to display the inventory to the owner and cashier in which quantity shows
def view_inventory():
    print("------------------------------Inventory------------------------------")
    print("Item Quantity Price")
    for item in inventory:
        if inventory[item][0] == 0:
            print(f"{item}: out of stock")
        else:
            print(f"{item} {inventory[item][0]}  Rs.{inventory[item][1]:.2f}")
# Function to display the inventory to the customer but it doesn't show quantity
def view_inventory_2():
    print("------------------------------Items------------------------------")
    print("Item \tPrice")
    for item in inventory:
        if inventory[item][0] == 0:
            print(f"{item}: out of stock")
        else:
            print(f"{item}:\tRs.{inventory[item][1]:.2f}")


# Function to calculate the total bill for the customer and also print the receipt
def calculate_bill():
    total = 0
    receipt = []
    while True:
        item_name = input("Enter the name of the item purchased by the customer/('done') to finish: ")
        if item_name == "done":
            break
        if item_name not in inventory:
            print("Item does not exist in inventory")
            continue
        quantity = int(input("Enter the quantity purchased: "))
        if inventory[item_name][0] == 0:
            print("Item is out of stock")
            continue
        if quantity > inventory[item_name][0]:
            print(f"Only {inventory[item_name][0]} {item_name} available")
            continue
        item_cost = quantity * inventory[item_name][1]
        total += item_cost
        receipt.append((item_name, quantity, item_cost))
        inventory[item_name] = (inventory[item_name][0] - quantity, inventory[item_name][1])
    
    # update text file
    write_inventory()
    # A Receipt will be print after done was input by the user
    print("\t---------------------Receipt---------------------")
    print("Item\tQuantity")
    for item in receipt:
        print(f"{item[0]}\t x {item[1]}\t= Rs.{item[2]:.2f}")
    print(f"Total: Rs.{total:.2f}")

# Main function
print("-------------------------Usama & Co. General Store-------------------------")
while True:
#Owner Menu
    print("\n1.Owner\n2.Cashier\n3.Customer")
    account_type = int(input("Enter account type: "))
    password = int(input("What is your account password: "))
    if account_type == 1 and password==767:
     # ask for action
     print("1.View Inventory\n2.Add New Item\n3.Add quantity\n4.Update price\n5.Remove Item\n6.Remove Quantity\n7.Exit")
     action = int(input("Enter your choice: "))
     
     if action == 1:
         view_inventory()
     elif action == 2:
         add_item()
     elif action == 3:
         add_quantity()
     elif action==4:
         update_price()
     elif action == 5:
         remove_item()
     elif action == 6:
         remove_quantity()
     elif action==7:
         break

     else:
         print("Invalid action.")

#Cashier Menu
    elif account_type == 2 and password==765:
        print("1.View Inventory\n2.Calculate Bill")
        choice=int(input("Enter your choice: "))
        if choice==1:
            view_inventory()
        elif choice==2:
            calculate_bill()
#Customer Menu 
    elif account_type == 3 and password==000:
        print("\t\tThank you for chosing us.\nHere are the items you can buy from our store\n")
        view_inventory_2()# Here is that inventory that belongs only to customer which shows inventory and price

else:
     print("Invalid account type.")
