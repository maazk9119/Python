import copy

Graph = {

    'A':{'O': 146, 'S': 140, 'C':494},
    'O':{'S': 151, 'A':146},
    'S':{'F': 99, 'R':80, 'A':140, 'O':151},
    'C':{'R': 146, 'A':494, 'P':138},
    'F':{'S': 99, 'B': 211},
    'R':{'C': 146, 'P':97, 'S':80},
    'B':{'F': 211, 'P':101}
}


def CalCost(new_path):
    
    new_cost = 0
    for index in range(1,len(new_path)):
        new_cost = new_cost + Graph[new_path[index-1]][new_path[index]]
    
    return new_cost



def UCS(graph, StartNode, EndNode):

    pqueue = []
    pqueue.append([ [StartNode], 0])
    
    while pqueue:
        path = pqueue.pop(0)
        node = path[0][-1]

        if node == EndNode:
            return path
        else:
            for everyneighbour in graph.get(node,[]):
                new_path = copy.deepcopy(path)
                new_path[0].append(everyneighbour)
                cost = CalCost(new_path[0])
                new_path[1] = (cost)
                pqueue.append(new_path)
            pqueue.sort(key = lambda x : x[1])

    return "None"

    
path = UCS(Graph, 'A','B')
print("The best route and it's cost is:",path)

