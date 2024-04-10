'''
students = {
	'mexico': 10,
	'colombia': 15,
	'puerto_rico': 4,
}

for country in students:
	print(country)

for country in students.keys():
    print(country)

for number_of_students in students.values():
    print(number_of_students)

for country, number_of_students in students.items():
	print(f'{country} : {number_of_students}')
'''      

x = 0.0
for i in range(10):
    x += 0.1

if x < 1.0 and x > 0.99999:
    print(f'x = {x}')
    # x = 0.9999999999999999
else:
    print(f'x != {x}')
    # x != 0.9999999999999999 ← floating point error