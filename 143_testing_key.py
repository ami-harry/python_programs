# testing key
# we can check whether a key is already exits in the dictionary or not, for this purpose we use membership operator.

# in, not in --> these are membership operator

stu = {101: 'shalini', 102: 'shalu', 103: 'keshav'}
# means yes or not? 101 dict me hai ye ni...yha to hai mtlb ye True dega
print(101 in stu)
print(105 in stu)  # mtlb 105 stu me hai? nahi hai 105 stu me to ye False dega
# mtlb kya 101 stu me nahi hai?  but yha to hai ye vala False dega
print(101 not in stu)
# mtlb 105 stu me nahi hai...ha ye to sahi hai...105 to ni hai stu de..ye True dega
print(105 not in stu)

# it will help while delete or insert new element
