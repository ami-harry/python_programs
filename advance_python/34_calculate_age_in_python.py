# calculating age
# take input
# dob(year, month,day)


from datetime import date

dob_year = int(input("Enter your dob year: "))
dob_month = int(input("Enter your dob month: "))
dob_date = int(input("Enter your dob date: "))
dob = date(dob_year, dob_month, dob_date)
t = date.today()  # it will give current date
# we will compare the today date with user input and will give by subtracting it

age = t.year-dob.year-((t.month, t.day) < (dob_month, dob_date))
print("your age is", age)
