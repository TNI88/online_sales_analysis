from product_manager import ProductManager
manager = ProductManager()
manager.add_product("Laptop", 3000, 5)
manager.add_product("Mouse", 150, 10)
manager.add_product("Tastatură", 250, 8)
manager.display_products()
print(f"Total Inventory Value: {manager.total_inventory_value()} RON")
from cart import Cart
cart = Cart()
cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])
cart.display_cart()
print(f"Total Cart Value: {cart.total_cart_value()} RON")
