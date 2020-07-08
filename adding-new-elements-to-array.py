# aadding new elements to arry using append method


import array as hk

arr=hk.array('i',[2,5,7,3,2,5,6,8,9])

for i in range(len(arr)):
    print("value at index no ",i,"is",arr[i])

print("out of loop")

arr.append(50)
arr.append(60)
arr.append(70)
arr.append(80)

print("the updated array is ")
for j in range(len(arr)):
    print("value at index no ",j,"is",arr[j])
