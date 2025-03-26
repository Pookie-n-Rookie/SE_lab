import sqlite3

def log_purchase(product_id, quantity, customer_name, price, db_name="store_inventory.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO purchase_history (product_id, quantity, customer_name, price)
                       VALUES (?, ?, ?, ?)''', (product_id, quantity, customer_name, price))
    conn.commit()

    with open("purchase_history.txt", "a") as file:
        file.write("Product ID: %d, Quantity: %d, Customer: %s, Price: %.2f\n" % (
            product_id, quantity, customer_name, price))

    conn.close()
    print("Purchase logged successfully.")

def print_purchase_history(db_name="store_inventory.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM purchase_history''')
    purchases = cursor.fetchall()
    if not purchases:
        print("No purchase history available.")
    else:
        for purchase in purchases:
            print("Purchase ID: %d, Product ID: %d, Quantity: %d, Customer Name: %s, Price: %.2f" % (
                purchase[0], purchase[1], purchase[2], purchase[3], purchase[4]))
    conn.close()
