# accessing nested dict using for loop

main_dic = {'course': 'python', 'fees': 1000,
            'dic1': {'course': 'java', 'fees': 12023}}

print("The original dict is")
print(main_dic)
print()

# printing all the keys manually
print("All keys of main dict using for loop:")
for i in main_dic:
    print(i)

print()
print("All values of main dict using for loop")
for i in main_dic:
    print(main_dic[i])
print()
print("all keys of maindict using keys method")
all_keys = main_dic.keys()
print(all_keys)
print()
print("all values of main dict using values method ")
all_values = main_dic.values()
print(all_values)

# printing the keys and values of nested dict inside main dict
print()
print("the original nested main dict is")
print(main_dic['dic1'])
print()
print("All keys of nested dict of main dict using for loop:")
for i in main_dic['dic1']:
    print(i)
print()
print("all the values of nested dict of main dict using for loop")
for i in main_dic['dic1']:
    print(main_dic['dic1'][i])
print()
print("all keys of nested dict of main dict using keys method")
all_keys_nested = main_dic['dic1'].keys()
print(all_keys_nested)
print()
print("all values of nested dict of main dict using values method")
all_values_nested = main_dic['dic1'].keys()
print(all_values_nested)
print()

# printing keys and values of whole nested loop using for loop
print()
print("printing keys and values of whole nested loop using for loop")
for i in main_dic:
    if type(main_dic[i]) is dict:
        for j in main_dic[i]:
            print(j, '=', main_dic[i][j])
    else:
        print(i, '=', main_dic[i])

print('done')

