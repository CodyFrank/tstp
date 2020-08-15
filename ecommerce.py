class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, inventpry, product):
        inventory_dict = inventory.inventory
        if product in inventory_dict:
            if inventory_dict[product] > 0:
                self.purchases.append(product)
                inventory_dict[product] -= 1
            else:
                print("We are out of stock")
        else:
            print("We don't have that product")

    def print_purchases(self):
        for item in self.purchases:
            print(item.name)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price



class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        if product not in self.inventory:
            self.inventory[product] = quantity
        else:
            self.inventory[product] += quantity

    def print_inventory(self):
        for key, value in self.inventory.items():
            print(key.name + ':' + str(value))




cust = Customer('Joe', 'joe@gmail.com')
# print(cust.name)
# print(cust.email)

apple_watch = Product('Apple Watch', 299)
# print(apple_watch.name)
# print(apple_watch.price)

mac = Product('mac', 1999)
# print(mac.name)
# print(mac.price)

inventory = Inventory()
inventory.add_product(apple_watch, 100)
# inventory.print_inventory()
inventory.add_product(mac, 498)
inventory.print_inventory()

cust.purchase(inventory, apple_watch)

cust.print_purchases()
inventory.print_inventory()