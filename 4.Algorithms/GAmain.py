from Genetic_Algorithm import Chromosome, Selection, Operator
import random


pop = [_ for _ in range(10)]
for i in range(len(pop)):
    pop[i] = Chromosome(8)
    print('Genes is:',pop[i].genes,'Fitness is',pop[i].fitness)

for g in range(0,1):
    select_child = []
    for person in pop:
        parents = Selection.binary_tournament(pop, 2, 5)
        print('First parent is:',parents[0].genes, 'Second parent is:', parents[1].genes)
        #child1,child2 = Operator.one_point_crossover(parents[0],parents[1])
        child1,child2 = Operator.two_point_crossover(parents[0],parents[1])
        if random.random() < 0.2:
            new_child = Operator.flipmutatuion(child1)
        if random.random() < 0.2:
            new_child = Operator.flipmutatuion(child2)

        select_child.append(child1)
        select_child.append(child2)

        new_pop = Selection.binary_tournament(pop+select_child, len(pop), 10)

print('Best solution found so far', sorted(new_pop, key=lambda x: x.fitness, reverse=True)[0].fitness)
