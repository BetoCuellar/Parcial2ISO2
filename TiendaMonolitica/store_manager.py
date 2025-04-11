from singleton_db import DatabaseConnection
from factory import ProductFactory

class StoreManager:
    def __init__(self):
        self.db = DatabaseConnection()
        self.factory = ProductFactory()
        self.products = []

    def add_product(self, type_, name, price):
        product = self.factory.create_product(type_, name, price)
        self.products.append(product)
        self.db.query(f"INSERT INTO productos (nombre, precio) VALUES ('{name}', {price})")

    def list_products(self):
        print("Productos en la tienda:")
        for product in self.products:
            product.display()

    def delete_product(self, name):
        self.products = [p for p in self.products if p.name != name]
        self.db.query(f"DELETE FROM productos WHERE nombre='{name}'")

    def update_price(self, name, new_price):
        for p in self.products:
            if p.name == name:
                p.price = new_price
        self.db.query(f"UPDATE productos SET precio={new_price} WHERE nombre='{name}'")

    def generate_report(self):
        print("Generando reporte de ventas ficticio...")

    def send_emails(self):
        print("Enviando emails a clientes ficticios...")

    def manage_inventory(self):
        print("Revisando inventario ficticio...")
