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

#Function with the default argument value 
def hello_fun(greeting, name='you'):
    return'{}, {}'.format(greeting, name)

print(hello_fun('Ola', 'Heena'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('math', 'art', name='Heena', phone='11223344')

#Finding out the days in given month of the year
days = [0,31,28,31,30,31,30,31,31,30,31,30,31,30,31]
#function to return the number of days of the month
def is_leap(year):
    """return true for leap year and false for semi leap year"""
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
        
    
def days_of_month(year, month):
    if(month<1 or month>12):
        return "invalid month entered"
    
    if(is_leap(year) and month==2):
        return 29
    
    return days[month]

print(days_of_month(2024, 2))


