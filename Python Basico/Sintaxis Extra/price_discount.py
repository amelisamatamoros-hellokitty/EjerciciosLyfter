print("----Calculate the price of your product----")
product_price=float(input("Please enter the price of your product: "))
while product_price<=0:
    product_price=int(input("This price is incorrect, please enter a new price: "))
if product_price<100:
    discount=0.02*product_price
else:
    discount=0.10*product_price
final_price=product_price-discount
print(f"Your discounted price for the product is: {final_price}")
