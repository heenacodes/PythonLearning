numbers = [1,2,3,4,5]

for num in numbers:
    if num==4:
        print('found!')
        continue
    print(num)


for num in numbers:
    for letter in 'abcd':
        print(num,letter)


for int in range(10):
    print(int)

for int in range(1, 6):
    print(int)

x=0
while x<=10:
    if x==7:
        print ('breaking')
        break
    print(x)
    x+=1