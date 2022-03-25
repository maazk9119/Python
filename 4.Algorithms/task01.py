import copy
class states:

    #Goal_state = []
    def __init__(self, representation):
        self.representation = representation

    def slide_left(self):
        new_state = states(copy.deepcopy(self.representation))
        empty_space = self.representation.index(0)
        if empty_space == 0 or empty_space == 3 or empty_space == 6:
            return new_state
        else:
            new_state.representation[empty_space - 1], new_state.representation[empty_space] = new_state.representation[empty_space], new_state.representation[empty_space - 1]
            return new_state

    def slide_right(self):
        new_state = states(copy.deepcopy(self.representation))
        empty_space = self.representation.index(0)
        if empty_space == 2 or empty_space == 5 or empty_space == 8:
            return new_state
        else:
            new_state.representation[empty_space+1], new_state.representation[empty_space] = new_state.representation[empty_space], new_state.representation[empty_space+1]
            return new_state

    def slide_up(self):
        new_state = states(copy.deepcopy(self.representation))
        empty_space = self.representation.index(0)
        if empty_space == 0 or empty_space == 1 or empty_space == 2:
            return new_state
        else:
            new_state.representation[empty_space-3], new_state.representation[empty_space] = new_state.representation[empty_space], new_state.representation[empty_space-3]
            return new_state

    def slide_down(self):
        new_state = states(copy.deepcopy(self.representation))
        empty_space = self.representation.index(0)
        if empty_space == 6 or empty_space == 7 or empty_space == 8:
            return new_state
        else:
            new_state.representation[empty_space+3], new_state.representation[empty_space] = new_state.representation[empty_space], new_state.representation[empty_space+3]
            return new_state

    def print_board(self):
        for i in range(len(self.representation)):
            if i%3 ==0:
                print('\n', end=' ')
            print(self.representation[i], end=' ')
        print('\n\n\n')

    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.
        """
        return [self.slide_left(), self.slide_right(), self.slide_up(), self.slide_down()]


    def BFS(self, GoalNode):
        queue = []
        queue.append([self.representation])

        while queue:
            path = queue.pop(0)
            node = path[-1]     
            self.representation = node

            if node == GoalNode:
                return path
            else:
                new_path = self.applyOperators()
                for sub_obj in new_path:
                    new_list = list(path)
                    new_list.append(sub_obj.representation)
                    queue.append(new_list)
            
        return "not found" 


#drive code...  
startNode = [2,8,3,1,6,4,7,0,5]
GoalNode  = [1,2,3,8,0,4,7,6,5]
Mystate = states(startNode)
path = Mystate.BFS(GoalNode)
print("\t \t Whole Path is:\n")
for i in path:
    print(i)
print("\nGoal node is:",path[-1])

