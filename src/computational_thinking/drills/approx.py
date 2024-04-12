objective = int(input('Insert a number: ')) # initial number to find the square root of
epsilon = 0.0001  # the range of possible acceptable error
step = epsilon**2   # the increment we'll use to achieve a number near our objective.
answer = 0.0    # our initial state of the answer
counter = 0

while abs(answer**2 - objective) >= epsilon and answer <= objective:
    # if the absolulte value of the difference between the square of our answer and our objective is greater or equal to the episilon AND the answer is less or equal to the objective then we will increment our answer
    answer += step
    counter += 1

if abs(answer**2 - objective) >= epsilon:   
    # when our squared answer minus the objective is greater than the epislon means that objective has no square root (precise) 
    print(f"the square root of {objective} wasn't found")
else:
    print(f'the approximated square root of {objective} is {answer} and it took {counter} iterations')
