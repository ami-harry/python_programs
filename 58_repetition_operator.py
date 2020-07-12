# repetition operator
# this operator is used to repeat the string for several times. it is denoted by *

# syntax --> string*no_of_times_to_print

str1 = "hariom \n"
print(str1 * 10)


# taking input string from the user and asking how many times do you want to print

inp_str = input("Enter your string: ")
no_of_time = int(input("Enter how many time you want to print the string: "))

output = (inp_str * no_of_time)
print(output)

# slicing of string
# string[start_index, end_index]
print("Enter the range to slice the string: ")
st_start = int(input("Enter the starting value "))
st_end = int(input("Enter the ending value "))
sc = inp_str[st_start:st_end]
print(sc)
