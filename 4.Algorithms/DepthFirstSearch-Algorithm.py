graph = {'A' : ['B','D'],
         'B' : ['C','E'],
         'D' : ['E','G','H'],
         'E' : ['C','F'],
         'G' : ['H']
        }



def DFS(graph, StartNode, GoalNode):
    stack = []
    stack.append(StartNode)

    while stack:
        path = stack.pop(-1)
        node = path[-1]

        if node == GoalNode:
            return path
        else:
            for eachSussor in graph.get(node,[]):
                newPath = list(path)
                newPath.append(eachSussor)
                stack.append(newPath)



#----------Main----------------#
print("This is DFS:")
print("It check in Depth")
print(DFS(graph,'A','F'))