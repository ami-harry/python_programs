# nested function()
# when we define one function inside another function , it is known as nested function or nesting of function.

# defining the nested function
def disp():
    def show():
        print("Show function ")
        # disp() if we call this inside this function it will give error after maximum time execution
    print("Display function")
    show()
    # print("Again Display function")


# calling the function
# disp()

# when the function will be called it will goto function name inside it find another its print statement and will print and in the next line another function is calling it will search for another function definition after finding it will execute that function also.. this is finction calling and defining inside function.


def out():
    def inn():
        print("This is inner function")
        out()
    print("This is outer function")
    inn()

# calling the function
# out()


# returning from nested function.

def out():
    def inn():
        return "this is inner function "
    result = inn() + "outer function"
    return result

# function calling
# print(out()) #printing directly
# a=out() #storing the returned value into a variable then printing the values
# print(a)


# function with returned value with parameter
def out(st):
    def inn():
        return "this is inner function "
    result = inn() + st + " outer function"
    return result


# calling function with arguments
a = out(" hello harry ")
print(a)
print(out(" hmmmm "))