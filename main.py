def ninja_intro(dict):
    for key, value in dict.items():
        print(f'i am {key} and i am {value} belt')

ninja = {}


name = input("enter your name")
belt = input("enter a belt colour")
ninja["name"] = name
ninja["belt"] = belt


ninja_intro(ninja)