products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
total_category_sales={}
for items_sold in products:
    category=items_sold["category"]
    price=items_sold["price"]
    if category in total_category_sales:
        total_category_sales[category]+=price
    else:
        total_category_sales[category]=price
print(total_category_sales)
    



