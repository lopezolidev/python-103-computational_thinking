objective = int(input('Select a number: ')) # number to find out the square root
epsilon = 0.0001
high = max(1.0, objective)
low = 0.0
answer = (high + low) / 2

while abs(answer**2 - objective) >= epsilon:
    if answer**2 < objective:
        low = answer
    else:
        high = answer

    answer = (high + low) / 2

print(f'The square root of {objective} is {answer}')
