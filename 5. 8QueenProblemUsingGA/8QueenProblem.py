import random
from math import exp
import copy


class Chorosome:

    def __init__(self, length):
        self.length = length
        self.genes = [None] * length
        for i in range(length):
            self.genes[i] = random.randint(1, 8)
        self.Evalutation()

    def Evalutation(self):
        self.fitness = 0
        for i in range(0, self.length):
            for j in range(i + 1, self.length):
                if self.genes[i] == self.genes[j]:
                    self.fitness += 1


class Selection:

    def binary_tournament(pop, no_of_person_select, toursize):
        new_population = []
        for i in range(no_of_person_select):
            Select_pop = []
            for j in range(toursize):
                Select_pop.append(random.choice(pop))

            new_population.append(min(Select_pop, key=lambda x: x.fitness))

        return new_population


class Operator:

    def one_point_crossover(parent1, parent2):
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)
        crossover_point = random.randint(0, len(parent2.genes))
        print("\nCrossOver point is:", crossover_point)
        child1.genes[crossover_point:] = parent2.genes[crossover_point:]
        child2.genes[crossover_point:] = parent1.genes[crossover_point:]
        print('\nChild one:', child1.genes, 'Child two', child2.genes)
        child1.Evalutation()
        child2.Evalutation()
        print('\nChild one fitness is:', child1.fitness, 'Child two fitness is:', child2.fitness)
        return child1, child2

    def flipmutatuion(child):
        index = 0
        for i in range(0, 8):
            for j in range(i + 1, 8):
                if child.genes[i] == child.genes[j]:
                    index = j
                    break
        if index != 0:
            child.genes[index] = random.randint(1, 8)
            child.Evalutation()

        return child


# Drive code
board = [_ for _ in range(0, 8)]
for i in range(8):
    board[i] = Chorosome(8)
    print(board[i].genes)

for i in range(8):
    print(board[i].fitness)

# generation loop till the peak found
while True:
    for queen in range(3):
        select_child = []
        print("Selected Parents are:")
        parents = Selection.binary_tournament(board, 2, 7)
        print(parents[0].genes)
        print(parents[1].genes)
        child1, child2 = Operator.one_point_crossover(parents[0], parents[1])

        if random.random() < 0.2:
            new_child_01 = Operator.flipmutatuion(child1)
            print("After mutation child one is:")
            print(new_child_01.genes)
            select_child.append(new_child_01)
        if random.random() < 0.2:
            new_child_02 = Operator.flipmutatuion(child2)
            print("After mutation child two is:")
            print(new_child_02.genes)
            select_child.append(new_child_02)
        else:
            select_child.append(child1)
            select_child.append(child2)

    new_board = Selection.binary_tournament(board + select_child, len(board), 10)
    board = new_board
    var = False
    for i in select_child:
        if i.fitness == 0:
            print("This is perfect representation that queen can not strike each other:")
            print("Board representation is:", i.genes)
            print("Its fitness is:", i.fitness)

            var = True
            break
    if var:
        break






