from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klass = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
if len(tutors) > len(klass):
    tutors_klass = zip_longest(tutors, klass)
else:
    tutors_klass = zip(tutors, klass)
print(type(tutors_klass))
print(*tutors_klass)
