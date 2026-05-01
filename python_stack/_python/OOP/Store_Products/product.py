class Product:

    _id_counter = 0

    def __init__(self,name,price,category):
        self.id = Product._id_counter
        Product._id_counter += 1

        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percentage_change, is_increased):
        if is_increased:
            self.price = self.price + (self.price * (percentage_change/100))
        else:
            self.price = self.price - (self.price * (percentage_change/100))

    def print_info(self):
        print(f"Product Name: {self.name}, Product Category: {self.category}, Product Price: {self.price}")