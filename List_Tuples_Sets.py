courses = ['Python', 'SQL', 'Snowflake', 'bdt']
print(courses[0:-1])

print(courses[2:])

courses.append('aws')
print(courses)

courses.insert(0,'confidence')
print(courses)

skills = ['consistency', 'practice', 'confidence']
courses.extend(skills)
print(courses)

popped=courses.pop(2)
print(popped)
print(courses)

#reversing the list
courses.reverse()
print(courses)

#sorting the list
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)

#finding if the value is in List
print(courses.index('confidence'))
print('Confidence' in courses)
print('confidence' in courses)

#Loop to print the list
for item in courses:
    print(item)

for index,item in enumerate(courses, start=3):
    print(index,item)

print(len(courses))

#joining the list in string and vice versa
courses_str = ' * '.join(courses);
print(courses_str)

courses = courses_str.split(' * ')
print(courses)

#immutable - Tuples
tuple1 = ('Heena', 'Shadab', 'Shadu')
tuple2 = tuple1
print(tuple1)
print(tuple2)
tuple1[0] = 'Honey' #tuple object does not support item assignment


#Sets
