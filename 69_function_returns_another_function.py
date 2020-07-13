# function returns another function

# a function can return another function

def disp():
    def show():
        # print("show function")
        return "show function"
    print("Display function ")
    # return "Display function"
    return show


val = disp()
print(val())
# if we didn't give val() then it will display the address of returning function
# disp() is returning a function so we have to call that function at the time of printing
print(val)


def disp(hk):
    print("\nthis is display function")
    return hk


def show():
    return "this is show function"


val = disp(show)
print(val())
print(val)
