# accessing nested dict using for loop

main_dict = {'first': {'course': 'python', 'fees': 56453, 'duration': '3months', 'dict1_inside_first': {'course': 'python_advance', 'fees': 6476}},
             'second': {'course': 'java', 'fees': 74352, 'teacher': 'harry', 'duration': '8 months'}, 'third': {'course': 'nodeJS', 'fees': 5342}}


print("the original main dict is")
print(main_dict)
print()

print("printing all id or main keys using for loop")
for id in main_dict:
    print(id)
print()

print("printing all values of id of main dict using for loop")
for val in main_dict:
    print(main_dict[val])
print()


print("printing all id of main dict using keys function")
all_keys = main_dict.keys()
print(all_keys)
print()


print("printing all id of main dict using values function")
all_vals = main_dict.values()
print(all_vals)
print()


print("printing all keys and values loop together using for loop")
for key in main_dict:
    for val in main_dict[key]:
        print(val, '=', main_dict[key][val])
print()
