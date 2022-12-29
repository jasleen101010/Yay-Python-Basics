cgpa = float(input("Enter your CGPA : "))
has_criminal_record = input("Do you have any Criminal Record? : ")

if cgpa >= 9.0 or has_criminal_record == "No":
    print("You're Eligible for Admission!")
else:
    print("You're ineligible for Admission!")