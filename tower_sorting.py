#!/usr/bin/env python
"""
Name of the author(s):
- Auguste Burlats <auguste.burlats@uclouvain.be>
"""
import copy
import time
import sys
from copy import deepcopy
from search import *


#################
# Problem class #
#################
class TowerSorting(Problem):

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        # return a list of tuple,
        # each tuple represent an action
        # for example (0, 1) move the top disk at column @0 on top of the column @1
        nb_towers = state.number
        max_size = state.size
        actions = []
        for i in range(nb_towers):
            if len(state.grid[i]) != 0:
                for j in range(nb_towers):
                    if i != j and len(state.grid[j]) != max_size:
                        # print((i,j))
                        yield (i,j)

    def result(self, state, action):
        # print("RESULT FUN DEBUG START")
        source = action[0]
        dest = action[1]
        # data = state.grid[source].pop(len(state.grid[source])-1)
        # return state.grid[dest].append(data)
        #newState = copy.deepcopy(state)

        newGrid = [list(col) for col in state.grid]
        move = "tower "+ str(action[0]) + " -> tower " + str(action[1])
        newState = State(state.number, state.size, newGrid, move)
        # print("newState before pop")
        data = newState.grid[source].pop()
        # print("newState debug after pop")
        newState.grid[dest].append(data)

        # newState.grid[source].remove(len(state.grid[source]) - 1)
        # print(newState.grid)
        # print("RESULT FUN DEBUG END")
        return newState


    def goal_test(self, state):
        visited = set()
        #print("goal test begin")
        for i in range(state.number):
            if len(state.grid[i]) == 0:
                continue
            if state.grid[i][0] in visited:
                return False
            if not all(int(x) == int(state.grid[i][0]) for x in state.grid[i]):
                #print("goal test : NOT A GOAL")
                #print(state.grid)
                return False
            visited.add(state.grid[i][0])
        #print("GOAL FOUND")
        #print(state.grid)
        return True




###############
# State class #
###############
class State:

    def __init__(self, number, size, grid, move="Init"):
        self.number = number
        self.size = size
        self.grid = grid
        self.move = move

    def __str__(self):
        s = self.move + "\n"
        for i in reversed(range(self.size)):
            for tower in self.grid:
                if len(tower) > i:
                    s += "".join(tower[i]) + " "
                else:
                    s += ". "
            s += "\n"
        return s

    def __eq__(self, other):
        if isinstance(other, State):
            return self.grid == other.grid
        return False

    def __hash__(self):
        grid_str = ''
        for i in range(self.number):
            grid_str += ''.join(self.grid[i])
        return hash(grid_str)


######################
# Auxiliary function #
######################
def read_instance_file(filepath):
    with open(filepath) as fd:
        lines = fd.read().splitlines()

    number_tower, size_tower = tuple([int(i) for i in lines[0].split(" ")])
    initial_grid = [[] for i in range(number_tower)]
    for row in lines[1:size_tower + 1]:
        elems = row.split(" ")
        for index in range(number_tower):
            if elems[index] != '.':
                initial_grid[index].append(elems[index])

    for tower in initial_grid:
        tower.reverse()

    return number_tower, size_tower, initial_grid


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: ./sort_tower.py <path_to_instance_file>")
    filepath = sys.argv[1]

    number, size, initial_grid = read_instance_file(filepath)

    init_state = State(number, size, initial_grid, "Init")
    problem = TowerSorting(init_state)
    # Example of search
    start_timer = time.perf_counter()
    node, nb_explored, remaining_nodes = breadth_first_graph_search(problem)
    end_timer = time.perf_counter()

    # Example of print
    path = node.path()

    for n in path:
        # assuming that the __str__ function of state outputs the correct format
        print(n.state)

    print("* Execution time:\t", str(end_timer - start_timer))
    print("* Path cost to goal:\t", node.depth, "moves")
    print("* #Nodes explored:\t", nb_explored)
    print("* Queue size at goal:\t", remaining_nodes)


