name = input("Enter Student Name: ")
roll_number = int(input("Enter Roll Number: "))
age = int(input("Enter Age: "))
math_marks = float(input("Enter Math marks: "))
science_marks = float(input("Enter Science marks: "))
english_marks = float(input("Enter English marks: "))

total_marks = math_marks + science_marks + english_marks
average = total_marks / 3
percentage = (total_marks / 300) * 100

print(f"\nName: {name}")
print(f"Roll Number: {roll_number}")
print(f"Age: {age}")
print(f"Math: {math_marks}")
print(f"Science: {science_marks}")
print(f"English: {english_marks}")
print(f"Total: {total_marks} / 300")
print(f"Average: {average:.2f}")
print(f"Percentage: {percentage:.2f} %")