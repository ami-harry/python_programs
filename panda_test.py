import pandas as pd


# taking details of student from the user:
name1 = input("Enter first student name: ")
age_1 = int(input(f"Enter the age for {name1}: "))
add_1 = input(f"Enter the address for {name1}: ")
print()
name2 = input("Enter second  student name: ")
age_2 = int(input(f"Enter the age for {name2}: "))
add_2 = input(f"Enter the address for {name2}: ")
print()

name3 = input("Enter third  student name: ")
age_3 = int(input(f"Enter the age for {name3}: "))
add_3 = input(f"Enter the address for {name3}: ")
print()

# combining the details in a variable
details = [[name1, age_1, add_1],
           [name2, age_2, add_2],
           [name3, age_3, add_3]]

# making data frame for the details and storing it into a variable named data_details
data_details = pd.DataFrame(
    details, columns=['Name', 'Age', 'Address'])

print(data_details)  # printing the details
