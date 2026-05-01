from store import Store
from product import Product

# Create store
my_store = Store("Tech Shop")

# Create products
p1 = Product("Laptop", 1000, "Electronics")
p2 = Product("Phone", 700, "Electronics")
p3 = Product("T-Shirt", 20, "Clothing")

# Add products
my_store.add_product(p1)
my_store.add_product(p2)
my_store.add_product(p3)

# Print products
p1.print_info()
p2.print_info()
p3.print_info()

print("\n--- Inflation 10% ---")
my_store.inflation(10)

for p in my_store.products:
    p.print_info()

print("\n--- Clearance on Electronics 20% ---")
my_store.set_clearance("Electronics", 20)

for p in my_store.products:
    p.print_info()

print("\n--- Sell Product (ID = 2) ---")
my_store.sell_product(2)

print("\n--- Remaining Products ---")
for p in my_store.products:
    p.print_info()