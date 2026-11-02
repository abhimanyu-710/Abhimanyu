
print("======================================================")
print("               SCHOOL RESULT PROCESSING")
print("======================================================")

student_name = input("Enter Student Name : ")
roll_number = int(input("Enter Roll Number : "))

print("\n--- Enter Marks for 5 Subjects (0-100) ---")

has_failed_subject = False
total_marks = 0

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    
    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100. Exiting.")
        exit()
        
    if mark < 40:
        has_failed_subject = True
        
    total_marks += mark

percentage = (total_marks / 500) * 100

if has_failed_subject:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remarks = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remarks = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remarks = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remarks = "Good"
    elif percentage >= 50:
        grade = "D"
        remarks = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remarks = "Pass"
    else:
        grade = "F"
        remarks = "Fail"

print("\n" + "=" * 54)
print("                 STUDENT REPORT CARD")
print("=" * 54)
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print("-" * 54)
print(f"Total Marks  : {total_marks} / 500.0")
print(f"Percentage   : {percentage:.2f}%")
print(f"Result       : {result}")
print(f"Grade        : {grade}")
print(f"Remarks      : {remarks}")
print("=" * 54)