
tuition_fee = float(input("Enter Tuition Fee: "))
lab_fee = float(input("Enter Lab Fee: "))
library_fee = float(input("Enter Library Fee: "))
exam_fee = float(input("Enter Exam Fee: "))
discount_amount = float(input("Enter Discount Amount: "))

total_fee = tuition_fee + lab_fee + library_fee + exam_fee
fee_after_discount = total_fee - discount_amount
annual_fee = fee_after_discount * 2
monthly_installment = annual_fee / 12

print(f"\nTuition Fee: {tuition_fee}")
print(f"Lab Fee: {lab_fee}")
print(f"Library Fee: {library_fee}")
print(f"Exam Fee: {exam_fee}")
print(f"Total Fee: {total_fee}")
print(f"Discount: {discount_amount}")
print(f"Fee after Discount: {fee_after_discount}")
print(f"Annual Fee: {annual_fee}")
print(f"Monthly Installment: {monthly_installment:.2f}")
