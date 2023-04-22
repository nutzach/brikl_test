class Product:
    def __init__(self, title, description, price, available_date, stock_quantity, images, category, is_promotional):
        self.title = title
        self.description = description
        self.price = price
        self.available_date = available_date
        self.stock_quantity = stock_quantity
        self.images = images
        self.category = category
        self.is_promotional = is_promotional

class Catalog:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

class Storefront:
    def __init__(self, name, products, catalogs):
        self.name = name
        self.products = products
        self.catalogs = catalogs

    def list_promotional_products(self):
        return [p for p in self.products if p.is_promotional == True]
    def search_by_catalog_name(self, name):
        for c in self.catalogs:
            if c.name == name:
                return c.products
            else:
                return []
    def search_by_category(self, category):
        return [p for p in self.products if p.category == category]
    def sort_by_newest(self):
        return sorted(self.products, key=lambda p: p.available_date, reverse=True)
    def sort_by_oldest(self):
        return sorted(self.products, key=lambda p: p.available_date)
    def filter_by_availability(self, available):
        return [p for p in self.products if p.stock_quantity > 0] if available else [p for p in self.products if p.stock_quantity == 0]
    
class MicroStore:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    def list_product_in_inventory(self):
        return self.inventory.products
    def search_by_category(self, category):
        return [p for p in self.products if p.category == category]
    def sort_by_newest(self):
        return sorted(self.products, key=lambda p: p.available_date, reverse=True)
    def sort_by_oldest(self):
        return sorted(self.products, key=lambda p: p.available_date)
    def filter_by_availability(self, available):
        return [p for p in self.products if p.stock_quantity > 0] if available else [p for p in self.products if p.stock_quantity == 0]

class Inventory:
    def __init__(self, name, products):
        self.name = name
        self.products = products