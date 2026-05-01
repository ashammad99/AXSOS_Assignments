from product import Product


class Store:
    def __init__(self, name):
        self.name = ""
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        for i, product in enumerate(self.products):
            if i == product.id:
                product.print_info()
                return self.products.pop(i)
            print("Product not found")
            return None

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
