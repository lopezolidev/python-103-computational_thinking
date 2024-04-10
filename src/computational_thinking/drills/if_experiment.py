name_1 = input("What's your name? ")
age_1 = int(input("What's your age? "))

name_2 = input("What's your name? ")
age_2 = int(input("What's your age? "))

if age_1 > age_2:
    print(f'{name_1} is older than {name_2}')
elif age_1 < age_2:
    print(f'{name_2} is older than {name_1}')
else:
    print(f'{name_1} and {name_2} are the same age')

    