number = int(input('Insert an integer: '))
answer = 0

while answer**2 < number:
    print(answer)
    answer += 1

if answer**2 == number:
    print(f'The root of {number} is {answer}')
else:
    print(f'{number} does not have an exact square root')