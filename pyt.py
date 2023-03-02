l = [['1', '1', '1', '1'], ['2', '2', '2', '2', '2'], ['3', '3', '3', '3', '3'], ['1']]
l1 = [[],['1', '1', '1', '1','1'], ['2', '2', '2', '2', '2'], ['3', '3', '3', '3', '3']]
l2 = [['1', '1'], ['2', '2'], ['3', '3']]
def goal_testbobr(state):
    nb_towers = 3
    for i in range(nb_towers):
        tower_len = len(state[i])
        if tower_len == 0:
            pass
        if tower_len == 2 :
            sample = state[i][0]
            for j in range(tower_len):
                if sample != state[i][j]:
                    return False
    return True

def goal_test(self, state):
    if state is None:
        return False
    nb_towers = state.number
    for i in range(nb_towers):
        tower_len = len(state.grid[i])
        if tower_len == 0:
            pass
        if tower_len == state.size :
            sample = state.grid[i][0]
            for j in range(tower_len):
                if sample != state.grid[i][j]:
                    return False
    return True

def goal_test(self, state):
    if state is None:
        return False
    tl = state.number
    ts = state.size
    for i in range(tl):
        if state.grid[i]: # not an empty list
            if not all(x == state.grid[i][0] for x in state.grid[i]) or len(state.grid[i]) != ts:
                return False
    return True

def newgoal_test(state):
    if state is None:
        return False
    nb_towers = 4
    print(state)
    for i in range(nb_towers):
        tower_len = len(state[i])
        if tower_len == 0:
            continue
        sample = state[i][0]
        for j in range(tower_len):
            if sample != state[i][j]:
                return False
    return True

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
                if not (all(x == state.grid[i][0] for x in state.grid[i])):
                    for j in range(nb_towers - 1):
                        if i != j:
                            actions.append((i, j))
        return actions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: ./sort_tower.py <path_to_instance_file>")
    filepath = sys.argv[1]

    number, size, initial_grid = read_instance_file(filepath)

    init_state = State(number, size, initial_grid, "Init")
    print(init_state)
    print(init_state.number)
    print(init_state.grid)
    print(init_state.move)
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
print(newgoal_test(l1))
