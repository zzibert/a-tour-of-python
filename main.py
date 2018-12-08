def belt_count(dict):
    belts = list(dict.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f"there are {num} {belt} belts")

# def ninja_intro(dict):
#     for key, value in dict.items():
#         print(f'i am {key} and i am {value} belt')

ninja = {}

while True:
    name = input("enter name")
    belt = input("enter belt")
    ninja[name] = belt
    if input("continue?") == "y":
        continue
    else:
        break


belt_count(ninja)