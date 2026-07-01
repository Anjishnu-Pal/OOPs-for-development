# json_sales_debug_demo.py
# Task: Compute total sales per product from JSON orders.
# Hidden bug: One JSON record has wrong product name: "Lapotp" instead of "Laptop".

import json

sales_json = '''
[
    {"order_id": 1, "product": "Laptop", "quantity": 2, "unit_price": 50000},
    {"order_id": 2, "product": "Mouse", "quantity": 5, "unit_price": 500},
    {"order_id": 3, "product": "Keyboard", "quantity": 3, "unit_price": 1500},
    {"order_id": 4, "product": "Laptop", "quantity": 1, "unit_price": 50000},
    {"order_id": 5, "product": "Mouse", "quantity": 2, "unit_price": 500},
    {"order_id": 6, "product": "Lapotp", "quantity": 1, "unit_price": 50000},
    {"order_id": 7, "product": "Keyboard", "quantity": 2, "unit_price": 1500}
]
'''
'''ABC'''
orders = json.loads(sales_json)

sales_per_product = {}

for order in orders:
    product = order["product"]
    quantity = order["quantity"]
    unit_price = order["unit_price"]

    order_total = quantity * unit_price

    if product not in sales_per_product:
        sales_per_product[product] = 0

    sales_per_product[product] += order_total

print("Total Sales Per Product")
print("-----------------------")

for product, total in sales_per_product.items():
    print(product, ":", total)