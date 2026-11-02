
print("====================================================")
print("             CALENDAR VERIFICATION SYSTEM")
print("====================================================")

year = int(input("Enter year: "))

if year <= 0:
    print("Error: Please enter a positive integer greater than 0[cite: 8].")
else:
    print("-" * 52)
    
    if year % 100 == 0:
        if year % 400 == 0:
            status = "LEAP YEAR"
            days_in_year = 366
            days_in_feb = 29
            reason = "Century year divisible by 400"
        else:
            status = "COMMON YEAR"
            days_in_year = 365
            days_in_feb = 28
            reason = "Century year not divisible by 400"
    else:
        if year % 4 == 0:
            status = "LEAP YEAR"
            days_in_year = 366
            days_in_feb = 29
            reason = "Divisible by 4 and not a century year"
        else:
            status = "COMMON YEAR"
            days_in_year = 365
            days_in_feb = 28
            reason = "Not divisible by 4"

