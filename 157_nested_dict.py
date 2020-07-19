# nested dict
# a dict inside dict

# creating an empty nested dict
# a = {1: {}, 2: {}, }
# print(type(a))


# creating nested dict

main_dic = {'course': 'python', 'fees': 1000,
            'dic1': {'course': 'java', 'fees': 12023}}

# accessing elements using keys
print("The original dict is")
print(main_dic)
print()
print(main_dic['course'])
print(main_dic['fees'])
print(main_dic['dic1']['course'])
print(main_dic['dic1']['fees'])
print()
print()

# adding element in main dic
main_dic['teacher'] = 'harry'

# adding element in nested dic1
main_dic['dic1']['teacher'] = 'hariom'
print()
print("the updated dict is")
print(main_dic)
print()
print()

# adding a new dict to main dict
main_dic['dic2'] = {'course': 'java script', 'fees': 8000}
print("the updated main dic is")
print(main_dic)
print("the dict was added")
print(main_dic['dic2'])
print()
print()
# adding a new dict to the nested dict1
main_dic['dic1']['dic2_inside_dic1'] = {
    'couse': 'machine learning', 'fees': 234566}

print()
print("Printing the updated dict")
print(main_dic)
print("the dict was added")
print(main_dic['dic1']['dic2_inside_dic1'])
print()
print()

# adding a new dict inside the dic2 of main dict
main_dic['dic2']['dic1_of_dic2'] = {'course': 'html', 'fees': 2000}
print("The updated dict is ")
print(main_dic)
print("The dict which was added is")
print(main_dic['dic2']['dic1_of_dic2'])
print()
print()


# adding one more dict insise the dic2 of dic1_of_dict2 of main dict
#
main_dic['dic2']['dic1_of_dic2']['dic2NdOf1'] = {'course': 'css', 'fees': 3000}
print("The updated dict is ")
print(main_dic)
print("The dict which was added is")
print(main_dic['dic2']['dic1_of_dic2']['dic2NdOf1'])
print()
print()

# adding one more dict insise the dic2 of dic1_of_dict2 of dic2NdOf1 main dict
main_dic['dic2']['dic1_of_dic2']['dic2NdOf1']['dic3Of1'] = {
    'course': 'jsp', 'fees': 4000}
print("The updated dict is ")
print(main_dic)
print("The dict which was added is")
print(main_dic['dic2']['dic1_of_dic2']['dic2NdOf1']['dic3Of1'])
print()
print()

# adding new element to main dic
main_dic['last_dict'] = {'this': 'is new', 'it will': 'be in', 'the': 'last'}
print("The updated dict is ")
print(main_dic)
print("The dict which was added is")
print(main_dic['last_dict'])
print()
