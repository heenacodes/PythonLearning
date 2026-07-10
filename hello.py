print("This is my first line of python code, yayyy")

def greet(name = 'Default'):
    print("hello", name)

greet()
greet("Heena")


def least_difference(a, b, c):
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    return min(diff1, diff2, diff3)

print(least_difference (1,10,10))

print()