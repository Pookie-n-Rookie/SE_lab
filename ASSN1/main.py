from inventory import InventoryManager

def customer_menu(inventory):
    while True:
        print("\nCustomer Menu:")
        print("1. View Products")
        print("2. Purchase Product")
        print("3. View Purchase History")
        print("4. Return to Main Menu")
        
        choice = raw_input("Enter your choice: ").strip()
        
        if choice == "1":
            inventory.list_products()
        
        elif choice == "2":
            inventory.list_products()
            try:
                product_id = int(raw_input("Enter product ID to purchase: "))
                quantity = int(raw_input("Enter quantity: "))
                customer_name = raw_input("Enter your name: ")
                
                # Get product details
                inventory.cursor.execute("SELECT quantity, price FROM products WHERE product_id=?", (product_id,))
                product = inventory.cursor.fetchone()
                
                if not product:
                    print("Invalid product ID!")
                    continue
                
                available_qty, price = product
                if quantity > available_qty:
                    print("Not enough stock available!")
                    continue
                
                # Update inventory
                new_qty = available_qty - quantity
                inventory.cursor.execute("UPDATE products SET quantity=? WHERE product_id=?", 
                                        (new_qty, product_id))
                inventory.conn.commit()
                
                # Log purchase
                from purchase_history import log_purchase
                log_purchase(product_id, quantity, customer_name, price * quantity)
                
                print("Purchase successful! Total: %.2f" % (price * quantity))
                
            except ValueError:
                print("Invalid input! Please enter numbers for ID and quantity.")
        
        elif choice == "3":
            from purchase_history import print_purchase_history
            print_purchase_history()
        
        elif choice == "4":
            break
        
        else:
            print("Invalid choice. Please try again.")

def seller_menu(inventory):
    while True:
        print("\nSeller Menu:")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. View Products")
        print("5. View Database")
        print("6. Return to Main Menu")
        
        choice = raw_input("Enter your choice: ").strip()
        
        if choice == "1":
            name = raw_input("Enter product name: ")
            try:
                quantity = int(raw_input("Enter quantity: "))
                price = float(raw_input("Enter price: "))
                inventory.add_product(name, quantity, price)
            except ValueError:
                print("Invalid input! Please enter numbers for quantity and price.")
        
        elif choice == "2":
            inventory.list_products()
            try:
                product_id = int(raw_input("Enter product ID to update
