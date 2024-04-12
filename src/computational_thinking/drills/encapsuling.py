def exhaustive(num):
    answer = 0
    while answer**2 < num:
        answer += 1

    if answer**2 == num:
        response = f'The root of {num} is {answer}'
    else:
        response = f'{num} does not have an exact square root'
    return response

def approx(num):
    epsilon = 0.01  # the range of possible acceptable error
    step = epsilon**2   # the increment we'll use to achieve a number near our objective.
    answer = 0.0    # our initial state of the answer
    counter = 0

    while abs(answer**2 - num) >= epsilon and answer <= num:
        # if the absolulte value of the difference between the square of our answer and our objective is greater or equal to the episilon AND the answer is less or equal to the objective then we will increment our answer
        answer += step
        counter += 1

    if abs(answer**2 - num) >= epsilon:   
        # when our squared answer minus the objective is greater than the epislon means that objective has no square root (precise) 
        response = f"the square root of {num} wasn't found"
    else:
        response = f'the approximated square root of {num} is {answer} and it took {counter} iterations'
    return response

def binary_s(num):
    epsilon = 0.001
    high = max(1.0, num)
    low = 0.0
    answer = (high + low) / 2

    while abs(answer**2 - num) >= epsilon:
        if answer**2 < num:
            low = answer
        else:
            high = answer
        answer = (high + low) / 2

    response = f'The square root of {num} is {answer}'
    return response

def algorithm_selector(op, num):
    sol = f'Sorry. {op} is not a valid option'
    if op == 1:
        sol = exhaustive(num)
    elif op == 2:
        sol = approx(num)
        #code
    elif op == 3:
        sol = binary_s(num)
        # code
    return sol
    
def start():
    print('Hello, this program finds the square root of a any positive number. \n It consist of 3 methods like so: \n 1. Exhaustive enumeration. \n 2. Approximation calculation \n 3. Binary search algorithm \n which one would you like to use?')
    
    option = int(input('Select the number of the algorithm: '))

    while option < 1 or option > 3:
        option = int(input('Sorry, that is not a valid option, choose an option between 1, 2 or 3: '))

    number = int(input('Choose a number: '))

    while number < 0:
        number = int(input('Sorry. That number is not a valid option, only positive integers: '))

    print(algorithm_selector(option, number))

start()