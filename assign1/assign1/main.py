from inventory import InventoryManager
from purchase_history import log_purchase, print_purchase_history

def customer_menu(inventory):
    while True:
        print("\nCustomer Menu")
        print("1. Make a Purchase")
        print("2. View Purchase History")
        print("3. Exit")

        choice = raw_input("Enter your choice: ").strip()

        if choice == "1":
            inventory.list_products()
            product_id = int(raw_input("Enter product ID to purchase: "))
            quantity = int(raw_input("Enter quantity: "))
            customer_name = raw_input("Enter your name: ")
            log_purchase(product_id, quantity, customer_name)
        
        elif choice == "2":
            print_purchase_history()
        
        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

def seller_menu(inventory):
    while True:
        print("\nSeller Menu")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. List Products")
        print("5. Exit")

        choice = raw_input("Enter your choice: ").strip()

        if choice == "1":
            name = raw_input("Enter product name: ")
            quantity = int(raw_input("Enter quantity: "))
            price = float(raw_input("Enter price: "))
            inventory.add_product(name, quantity, price)
        
        elif choice == "2":
            product_id = int(raw_input("Enter product ID: "))
            quantity = int(raw_input("Enter new quantity: "))
            price = float(raw_input("Enter new price: "))
            inventory.update_product(product_id, quantity, price)
        
        elif choice == "3":
            product_id = int(raw_input("Enter product ID to remove: "))
            inventory.remove_product(product_id)
        
        elif choice == "4":
            inventory.list_products()
        
        elif choice == "5":
            break
        
        else:
            print("Invalid choice. Please try again.")

def main():
    inventory = InventoryManager()

    while True:
        print("\nWelcome to the Inventory Management System")
        print("1. Login as Customer")
        print("2. Login as Seller")
        print("3. Exit")

        role_choice = raw_input("Enter your choice: ").strip()

        if role_choice == "1":
            customer_menu(inventory)
        
        elif role_choice == "2":
            seller_menu(inventory)
        
        elif role_choice == "3":
            inventory.close()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

