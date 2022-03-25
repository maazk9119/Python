import copy
import random
import string

def random_passowrd():
    return[random.choice(string.printable) for i in range(10)]

def Evaluate(sol, target):
    target_list = list(target)
    difference = 0
    for i in range(len(target_list)):
        s = sol[i]
        t = target_list[i]
        difference += abs(ord(s) - ord(t))
    return difference

def mutate(sol):
    i = random.randint(0, len(sol)-1)
    sol[i] = random.choice(string.printable)

#Drive code
password = input("Enter password with 10digits:")
if len(password) == 10:
    solution = random_passowrd()
    score = Evaluate(solution, password)
    while True:
        print('Best password match so far:',solution, 'with cost:',score)
        if score == 0:
            break
        else:
            sol = copy.deepcopy(list(solution))
            mutate = (sol)
            new_score = Evaluate(sol, password)
            if new_score < score:
                score = new_score
                solution = sol
else:
    print("Try again wrong password size")