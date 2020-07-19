# nested dictionay having the values as only a dict
# in the last nested dict the elements we in key value and element as a dict also
# in this dict the elements are only as dict

main_dict = {'first': {'course': 'python', 'fees': 56453},
             'second': {'course': 'java', 'fees': 74352}}

print('the original dict is')
print(main_dict)
print()
print('first dict of nested dict')
print(main_dict['first'])
print()
print('second dict of nested dict')
print(main_dict['second'])
print()

# accessing the element of nested dict
print(main_dict['first']['course'])
print(main_dict['first']['fees'])
print(main_dict['second']['course'])
print(main_dict['second']['fees'])

# addding new values in the nested dict
print('the original nested first dict is')
print(main_dict['first'])
# updating this
main_dict['first']['teacher'] = 'harry'
main_dict['first']['duration'] = '6 months'
print()
print("The updated first nested dict is")
print(main_dict['first'])
print()

# updating the second nested dict
print('the original nested second dict is')
print(main_dict['second'])
# updating this
main_dict['second']['teacher'] = 'hariom'
main_dict['second']['duration'] = '8 months'
print()
print("The updated second nested dict is")
print(main_dict['second'])
print()

# modifying the previous values of nested dict
print("Before modification the  nested dict first is")
print(main_dict['first'])
# modifying it
main_dict['first']['duration'] = '3months'
print("The updated nested dict first is")
print(main_dict['first'])
print()
# modifying the previous values of nested dict
print("Before modification the  nested dict second is")
print(main_dict['second'])
# modifying it
main_dict['second']['teacher'] = 'harry'
print("The updated nested dict second is")
print(main_dict['second'])
print()

# deleting element
print("Defore deletion the nested first dict is")
print(main_dict['first'])
del main_dict['first']['teacher']
print("after deletion the first nested dict is")
print(main_dict['first'])
print()


# adding a new dict  in main dict
main_dict['third'] = {'course': 'nodeJS', 'fees': 5342}
print("The updated main dict is")
print(main_dict)
print("the added dict was")
print(main_dict['third'])
print()

# adding a dict inside nested dict first
print('before addition the first nested dict is')
print(main_dict['first'])
main_dict['first']['dict1_inside_first'] = {
    'course': 'python_advance', 'fees': 6476}
print("The updated first nested dict  is")
print(main_dict['first'])
print()
print("The updated main dict is")
print(main_dict)
print()
