
import math

print("====================================================")
print("               ENGINEERING CALCULATION TOOL")
print("====================================================")

value = float(input("Enter a numerical value: "))

exponent = float(input("Enter an exponent: "))
power_result = math.pow(value, exponent)

sqrt_result = math.sqrt(value)

decimal_measurement = float(input("Enter a decimal measurement: "))
ceil_result = math.ceil(decimal_measurement)
floor_result = math.floor(decimal_measurement)

print("\n--- Results ---")
print(f"Value            : {value}")
print(f"Exponent         : {exponent}")
print(f"Power (pow)      : {power_result}")
print(f"Square Root (sqrt) : {sqrt_result:.4f}")
print(f"Decimal Value    : {decimal_measurement}")
print(f"Ceil Value       : {ceil_result}")
print(f"Floor Value      : {floor_result}")
print("====================================================")