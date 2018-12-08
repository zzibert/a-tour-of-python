grades = ['A', 'B', 'C', 'F', 'A', 'F', 'D', 'F']


def func(grade):
    return grade != 'F'

print(list(filter(func, grades)))