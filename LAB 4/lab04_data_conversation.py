print("=" * 52)
print("                    DATA CONVERSION UTILITY")
print("=" * 52)

product_name = input("Enter Product Name : ")

price = float(input("Enter Price        : "))

# 3. Take quantity as input and convert it to int
quantity = int(input("Enter Quantity     : "))







total_price = price * quantity

amount_str = str(total_price)

print("\n" + "-" * 52)
print("                TYPE CASTING SUMMARY")
print("-" * 52)
print(f"{'Variable':<20} {'Value':<18} {'Python Type'}")
print("-" * 52)
print(f"{'product_name':<20} {product_name:<18} {type(product_name)}")
print(f"{'price':<20} {price:<18} {type(price)}")
print(f"{'quantity':<20} {quantity:<18} {type(quantity)}")
print(f"{'total_price':<20} {total_price:<18} {type(total_price)}")
print(f"{'amount_str':<20} {amount_str:<18} {type(amount_str)}")
print("-" * 52)

print("\n" + " " * 24 + "TAX INVOICE")
print("-" * 52)
print(f"Product Name       : {product_name}")
print(f"Price per Unit     : Rs. {price}")
print(f"Quantity           : {quantity}")
print("-" * 52)
print(f"Invoice Total      : Rs. {amount_str}")
print("=" * 52)