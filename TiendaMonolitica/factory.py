class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Producto: {self.name}, Precio: ${self.price}")

class Laptop(Product):
    def display(self):
        print(f"Laptop: {self.name}, Precio: ${self.price}")

class Smartphone(Product):
    def display(self):
        print(f"Smartphone: {self.name}, Precio: ${self.price}")

class ProductFactory:
    def create_product(self, type_, name, price):
        if type_ == "laptop":
            return Laptop(name, price)
        elif type_ == "smartphone":
            return Smartphone(name, price)
        else:
            return Product(name, price)
