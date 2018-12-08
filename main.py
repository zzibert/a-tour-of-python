name = "ryuuuu"

def print_name():
    global name
    name = "ryu"
    print("the name inside the function is", name)

print_name()
print("outside the function the name is:", name)
