
print("=" * 44)
print("        CLOTHING STORE BILLING SYSTEM")
print("=" * 44)

customer_name = input("Enter Customer Name: ")

garment_name = input("Enter Garment Name: ")

price_per_unit = float(input("Enter Price of one garment: "))

quantity = int(input("Enter Number of Garments: "))

total_amount = price_per_unit * quantity

print("\n" + "=" * 44)
print("                    BILL")
print("=" * 44)
print(f"Customer Name   : {customer_name}")
print(f"Garment Name    : {garment_name}")
print(f"Price per Unit  : Rs. {price_per_unit}")
print(f"Quantity        : {quantity}")
print(f"Total Amount    : Rs. {total_amount}")
print("=" * 44)