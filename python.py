name = input("Enter your name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA (0-5): "))
field = input("Enter your field of interest: ")
graduated = input("Have you graduated? (yes/no): ").strip().lower()

print("\n===== User Information =====")
print(f"Name           : {name}")
print(f"Age            : {age}")
print(f"GPA            : {gpa:.2f}")
print(f"Field of Interest: {field}")
print(f"Graduated      : {'Yes' if graduated == 'yes' else 'No'}")
print("============================\n")

eligible_scholarship = age < 25 and gpa >= 3.5 and graduated == "yes"
eligible_internship = age < 30 and gpa >= 2.5

if eligible_scholarship:
    print("You are eligible for a scholarship!")
elif eligible_internship:
    print(" You are eligible for an internship!")
else:
    print(" You are not eligible at the moment. Please apply again later.")
