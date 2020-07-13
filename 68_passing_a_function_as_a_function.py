# passing a function to a function as a parameter
# we can pass a function as a parameter to another function

def out(argu):
    print("outer function " + argu())


def inn():
    return "hello"


out(inn)


def disp(hk):
    return "hi this is outer function\n" + hk()


def show():
    return "this is paramter value after passing the function as argument"


res = disp(show)
print(res)
