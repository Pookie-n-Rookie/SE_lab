import sqlite3
import os

class InventoryManager:
    def __init__(self, db_name="store_inventory.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS purchase_history (
            purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity INTEGER NOT NULL,
            customer_name TEXT NOT NULL,
            price REAL NOT NULL,
            FOREIGN KEY(product_id) REFERENCES products(product_id)
        )''')

        self.conn.commit()

    def add_product(self, name, quantity, price):
        self.cursor.execute('''INSERT INTO products (name, quantity, price)
                               VALUES (?, ?, ?)''', (name, quantity, price))
        self.conn.commit()
        print("Product '%s' added successfully." % name)

    def update_product(self, product_id, quantity, price):
        self.cursor.execute('''UPDATE products SET quantity = ?, price = ? WHERE product_id = ?''',
                            (quantity, price, product_id))
        self.conn.commit()
        print("Product %d updated successfully." % product_id)

    def remove_product(self, product_id):
        self.cursor.execute('''DELETE FROM products WHERE product_id = ?''', (product_id,))
        self.conn.commit()
        print("Product %d removed successfully." % product_id)

    def list_products(self):
        self.cursor.execute('''SELECT * FROM products''')
        products = self.cursor.fetchall()
        if not products:
            print("No products available.")
        else:
            for product in products:
                print("Product ID: %d, Name: %s, Quantity: %d, Price: %.2f" % (
                    product[0], product[1], product[2], product[3]))
    
    def print_database(self):
        print("\n--- PRODUCTS TABLE ---")
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()
        for product in products:
            print("ID: %d, Name: %s, Qty: %d, Price: %.2f" % product)
        
        print("\n--- PURCHASE HISTORY TABLE ---")
        self.cursor.execute("SELECT * FROM purchase_history")
        purchases = self.cursor.fetchall()
        for purchase in purchases:
            print("Purchase ID: %d, Product ID: %d, Qty: %d, Customer: %s, Price: %.2f" % purchase)

    def close(self):
        self.conn.close()
