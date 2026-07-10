
from my_module import find_index, test
import random
import datetime, calendar, os



subjects = ['English', 'Math', 'Python', 'SQL']

index = find_index('SQL', subjects)
#index = mm.find_index('SQL', subjects)
print(index)

print(test)

random_subject = random.choice(subjects)
print(random_subject)

print(datetime.date.today())
print(calendar.isleap(2021))


print(os.getcwd())
subjects.t


