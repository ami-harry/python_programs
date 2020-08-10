# directry information
# take input from the user and give him all the contents of that directry


import os
print("Enter . for current directry or enter the directly name to see the details")
ch = input("Enter which directry content you want to see: ")
data = os.walk(ch, topdown=False)
for files in data:
    print(files, end='\n\n')
print("Everything done sucessfully")
