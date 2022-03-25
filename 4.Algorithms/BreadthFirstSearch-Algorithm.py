graph = {'A' : ['B','D'],
         'B' : ['C','E'],
         'D' : ['E','G','H'],
         'E' : ['C','F'],
         'G' : ['H']
        }


def BFS(graph, StartNode, GoalNode):
    queue = []
    queue.append(StartNode)
    while queue:
        path  = queue.pop(0)
        node = path[-1]
        if node == GoalNode:
            return path
        else:
            for everySuccessor in graph.get(node,[]):
                newPath = list(path)
                newPath.append(everySuccessor)
                queue.append(newPath)



#----------------Main-------------------------
print("This is BFS:")
print("It check in breadth:")
print(BFS(graph,'A','F'))