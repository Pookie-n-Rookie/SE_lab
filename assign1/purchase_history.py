import sqlite3
import time

def log_purchase(product_id, quantity, customer_name, db_name="store_inventory.db"):
    timestamp = time.time()
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO purchase_history (product_id, quantity, timestamp, customer_name)
                       VALUES (?, ?, ?, ?)''', (product_id, quantity, timestamp, customer_name))
    conn.commit()

    with open("purchase_history.txt", "a") as file:
        file.write("Product ID: {}, Quantity: {}, Customer: {}, Timestamp: {}\n".format(
            product_id, quantity, customer_name, timestamp))

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
            print("Purchase ID: {}, Product ID: {}, Quantity: {}, Timestamp: {}, Customer Name: {}".format(
                purchase[0], purchase[1], purchase[2], purchase[3], purchase[4]))
    conn.close()

