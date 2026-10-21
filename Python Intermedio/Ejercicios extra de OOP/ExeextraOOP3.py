class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

class Inventory:
    def __init__(self):
        self.product_list=[]
    

    def add_product(self,product):
        self.product_list.append(product)


    def show_products(self):
        for item,product in enumerate(self.product_list):
            print(f"Product {item+1}: {product.name}, 'Price {product.price}', 'Quantity: {product.quantity}")


    def total_value_inventory(self):
        total_inventory=0
        for product in self.product_list:
            total_inventory+=product.price*product.quantity
        return total_inventory



product_1 = Product("Mouse", 5000, 3)
product_2 = Product("Teclado", 8000, 2)
inventory_1=Inventory()
inventory_1.add_product(product_1)
inventory_1.add_product(product_2)
inventory_1.show_products()
print(f'Total inventory value: {inventory_1.total_value_inventory()}')


