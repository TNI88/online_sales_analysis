from product_manager import ProductManager
manager = ProductManager()
manager.add_product("Laptop", 3000, 5)
manager.add_product("Mouse", 150, 10)
manager.add_product("Tastatură", 250, 8)
manager.display_products()
print(f"Total Inventory Value: {manager.total_inventory_value()} RON")
