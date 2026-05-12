def multiply(x):
    return x * 5

def call(fun, arg):
    return fun(arg)


def square_call(fun, arg):
    return(fun(fun(arg)))


print(
    call(multiply, 5),
    square_call(multiply,5),
    sep= '\n'
)

def mod_of_five(arg):
    """ Returns the reminder od arg after deviding by 5"""
    return arg % 5

print(
    'Which number is biggest',
    max(12, 18, 15),
    'Which number is biggest modulo 5',
    max(56, 60, 64, key=mod_of_five),
    sep='\n'
)

print('the area of India is', round(25875647887, -3))

def is_odd(num):
    return num%2==1

print(is_odd(5))