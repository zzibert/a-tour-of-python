def cough_dec(func):
    def func_wrapper():
        #code before function
        print('*cough*')
        func()
        #code after function
        print('*cough*')
    return func_wrapper

@cough_dec
def question():
    print('can you give me a discount on that?')
@cough_dec
def answer():
    print("its only 50p you cheap fuck")

question()
answer()