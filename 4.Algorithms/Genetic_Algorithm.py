import random
from math import exp
import copy

class Chromosome:

    def __init__(self, length):
        self.genes = [None]*length
        for i in range(length):
            self.genes[i] = random.randint(0,1)

        self.Evalutation()

    def Evalutation(self):
        x_axis = 4*self.genes[1] + 2*self.genes[2] + 1*self.genes[3]
        y_axis = 4*self.genes[-3]+ 2*self.genes[-2] + 1*self.genes[-1]

        if self.genes[0]:
            x_axis = -1*x_axis
        
        if self.genes[-4]:
            y_axis = -1*y_axis

        self.fitness = (exp(-1*(pow(x_axis, 2)+pow(y_axis, 2)))+(2*exp(-1*(pow(x_axis-1.7,2)+pow(y_axis-1.7,2)))))
        return self.fitness

        
class Selection:

    def binary_tournament(pop, no_of_person_select, toursize):
        new_population = []
        for i in range(no_of_person_select):
            Select_pop = []
            for j in range(toursize):
                Select_pop.append(random.choice(pop))

            new_population.append(max(Select_pop, key=lambda x:x.fitness))

        return new_population

class Operator:

    def one_point_crossover(parent1, parent2):
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)   

        crossover_point = random.randint(0,len(parent2.genes))
        print("\nCrossOver point is:",crossover_point)
        child1.genes[crossover_point:] = parent2.genes[crossover_point:]
        child2.genes[crossover_point:] = parent1.genes[crossover_point:]
        print('\nChild one:',child1.genes,'Child two',child2.genes)
        child1.Evalutation()
        child2.Evalutation()
        print('\nChild one fitness is:',child1.fitness, 'Child two fitness is:',child2.fitness)
        return child1,child2


    def two_point_crossover(parent1, parent2):
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)

        crossover_point01 = random.randint(0, len(parent2.genes))
        crossover_point02 = random.randint(0, len(parent2.genes))

        if crossover_point01 > crossover_point02:
            crossover_point01,crossover_point02 = crossover_point02,crossover_point01
        print('\nCrossOver one is:', crossover_point01, '\nCrossOver two is:',crossover_point02)

        child1.genes[crossover_point01:crossover_point02] = parent2.genes[crossover_point01:crossover_point02]
        child2.genes[crossover_point01:crossover_point02] = parent1.genes[crossover_point01:crossover_point02]
        print('Child One is:',child1.genes, 'Child two is:',child2.genes)

        child1.Evalutation()
        child2.Evalutation()

        print('Child one fitness is:',child2.fitness)
        print('Child two fitness is:', child1.fitness)

        return child1,child2


    def flipmutatuion(child):
        index = random.randint(0,len(child.genes)-1)
        print("Index is:",index)
        print("Before mutation")
        print("Child Genes is:",child.genes)
        child.genes[index] = int(not(child.genes[index]))
        print("After Mutation:")
        print("Child Genes is:",child.genes)

        child.Evalutation()

        return child


