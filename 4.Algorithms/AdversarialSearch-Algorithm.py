import copy

graph = {
    'A': {'B': 9, 'C': 4, 'D': 7},
    'B': {'A': 9, 'E': 11},
    'C': {'A': 4, 'E': 17, 'F': 12},
    'D': {'A': 7, 'F': 14},
    'E': {'B': 11, 'C': 17, 'Z': 5},
    'F': {'C': 12, 'D': 14, 'Z': 9}
}

heuristic = {
    'A': 21,
    'B': 14,
    'C': 18,
    'D': 18,
    'E': 5,
    'F': 8,
    'Z': 0
}


def CalCost(new_path):
    
    new_cost = 0
    for index in range(1,len(new_path)):
        new_cost = new_cost + graph[new_path[index-1]][new_path[index]]
    
    return new_cost



def Astar(graph, StartNode, EndNode):

    pqueue = []
    pqueue.append([ [StartNode], heuristic[StartNode]])
    
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
                next_heusritic = heuristic[everyneighbour]
                new_path[1] = (cost + next_heusritic)
                pqueue.append(new_path)
            pqueue.sort(key = lambda x : x[1])

    return "None"

    
path = Astar(graph, 'A','Z')
print("The best route and it's cost is:",path)

