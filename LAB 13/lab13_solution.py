
print("====================================================")
print("             INVENTORY CONTROL SYSTEM")
print("====================================================")

inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:
    print("\nSelect an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        print("\n--- Current Inventory ---")
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")
            
    elif choice == '2':
        new_item = input("Enter item name to add: ")
        inventory.append(new_item)
        print(f"[SUCCESS] \"{new_item}\" added to inventory.")
        
    elif choice == '3':
        item_to_remove = input("Enter item name to remove: ")
        if item_to_remove in inventory:
            inventory.remove(item_to_remove)
            print(f"[SUCCESS] \"{item_to_remove}\" removed from inventory.")
        else:
            print(f"[ERROR] \"{item_to_remove}\" not found in inventory.")
            
    elif choice == '4':
        inventory.sort()
        print("\n[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")
            
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
        
    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 5.")