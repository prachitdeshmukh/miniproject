from datetime import date

# Input
name = input("Enter your name: ")
dob = input("Enter your Date of Birth (DD/MM/YYYY): ")

# Convert input into day, month, year
day, month, year = map(int, dob.split("/"))

birth_date = date(year, month, day)
today = date.today()

# Calculate age in years
age = today.year - birth_date.year

# Check if birthday has occurred this year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

# Calculate total days lived
days_lived = (today - birth_date).days

# Calculate total months lived
months_lived = age * 12 + (today.month - birth_date.month)

if today.day < birth_date.day:
    months_lived -= 1

# Display result
print("\n------ Age Details ------")
print("Name          :", name)
print("Date of Birth :", birth_date.strftime("%d/%m/%Y"))
print("Age           :", age, "years")
print("Months Lived  :", months_lived, "months")
print("Days Lived    :", days_lived, "days")