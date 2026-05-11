student = {'Name': 'Heena', 'Age': '35', 'subjects': ['Python', 'SQL']}
print(student['Name'])
print(student['subjects'])

#print(student['phone']) #throws error when key is not present

print(student.get('Name'))
print(student.get('phone', 'Not found'))

#Adding new key and its value
student['phone'] = '00001111' 
print(student.get('phone', 'Not found'))

#Updating/overriting the value for the existing key
student['Name'] = 'Honey' 
print(student)

#Updating many keys at once
student.update({'Name': 'Shadab', 'Age':'38', 'phone': '11112222'})
print(student)

#deleting the key
del student['phone']
print(student)

print(student.pop('Age'))
print(student)

print(len(student)) 
print(student.values())
print(student.keys())
print(student.items())

for key, values in student.items():
    print(key)
    print(values)



