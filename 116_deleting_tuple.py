# deleting tuple
# as tuple is immutable object we cant delete its elements
# we can achieve it with the help of slicing and concatination.

a = (34, 32, 'hk', 'sj', 34, 234)
# here we want to remove sj(position no 3) we will slice the original tuple into two parts then we will add those two slices and will print the new one
sl_1 = a[:3]
sl_2 = a[4:]
final = sl_1+sl_2
print("The original tuple was ", a)
print("The modified  tuple  after deletion  ", final)
