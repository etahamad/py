# You are working for the school Principal. We have a database of school students:
school = {'Bobby', 'Tammy', 'Jammy', 'Sally', 'Danny'}

# during class, the teachers take attendance and compile it into a list.
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

# using what you learned about sets, create a piece of code that the school principal can use to immediately find out who missed class so they can call the parents.
print('Students who missed class: ' + str(school.difference(attendance_list)))

# Another example to get red of the {'something'} notation:
missed_list = school.difference(attendance_list)
for student in missed_list:
    print(student + ' is a missed student')
    print('\n')
