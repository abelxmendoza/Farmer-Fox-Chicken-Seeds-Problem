"""

#######                                           #######                       #####                                                                       #####                              
#         ##   #####  #    # ###### #####         #        ####  #    #        #     # #    # #  ####  #    # ###### #    #          ##   #    # #####     #     # ###### ###### #####   ####  
#        #  #  #    # ##  ## #      #    #        #       #    #  #  #         #       #    # # #    # #   #  #      ##   #         #  #  ##   # #    #    #       #      #      #    # #      
#####   #    # #    # # ## # #####  #    #        #####   #    #   ##          #       ###### # #      ####   #####  # #  #        #    # # #  # #    #     #####  #####  #####  #    #  ####  
#       ###### #####  #    # #      #####  ###    #       #    #   ##   ###    #       #    # # #      #  #   #      #  # # ###    ###### #  # # #    #          # #      #      #    #      # 
#       #    # #   #  #    # #      #   #  ###    #       #    #  #  #  ###    #     # #    # # #    # #   #  #      #   ## ###    #    # #   ## #    #    #     # #      #      #    # #    # 
#       #    # #    # #    # ###### #    #  #     #        ####  #    #  #      #####  #    # #  ####  #    # ###### #    #  #     #    # #    # #####      #####  ###### ###### #####   ####  
                                           #                            #                                                   #                                                                  



This Python script solves the Farmer, Fox, Chicken, and Seeds problem using the Breadth-First Search (BFS) algorithm.
The problem involves moving the Farmer, Fox, Chicken, and Seeds from one side of the river to the other while adhering to the following constraints:
1. The Farmer must be present for the boat to move.
2. The Fox cannot be left alone with the Chicken.
3. The Chicken cannot be left alone with the Seeds.

The script defines the problem, implements BFS to explore the state space, and finds the optimal solution, ensuring the shortest path to the goal state.

Output:
- If a solution is found, it displays the sequence of states representing the steps to solve the problem.
- If no solution exists, it indicates that no solution was found.
"""



from collections import deque

# Define the initial and goal states
initial_state = ("A", "FFCSB")  # Initial side with Farmer, Fox, Chicken, Seeds, Boat
goal_state = ("B", "FFCSB")     # Goal side, identical to initial

# Define a function to check if a state is valid
def is_valid(state):
    farmer, otherside = state

    # Check constraints to determine if the state is valid
    if "F" in otherside and "C" in otherside and "S" not in otherside:
        return False  # Chicken would be eaten
    if "F" in otherside and "C" not in otherside and "S" in otherside:
        return False  # Seeds would be eaten
    return True

# Define the BFS algorithm
def bfs():
    visited = set()
    queue = deque([(initial_state, [])])  # Initialize the queue with the initial state and an empty path

    while queue:
        current_state, path = queue.popleft()  # Get the current state and path

        if current_state == goal_state:
            return path  # Return the solution path

        if current_state not in visited:
            visited.add(current_state)

            # Generate possible next states based on the current side of the river (A or B)
            farmer, otherside = current_state
            next_states = []

            if farmer == "A":
                next_states.append(("B", otherside))
            else:
                next_states.append(("A", otherside))

            for item in "FCS":
                if item in otherside:
                    next_states.append((farmer, otherside.replace(item, "")))

            for next_state in next_states:
                if is_valid(next_state):
                    queue.append((next_state, path + [next_state]))

    return None  # No solution found

# Solve the problem
solution = bfs()

if solution:
    print("Solution found. Path:")
    for state in solution:
        print(f"Side: {state[0]}, Items: {state[1]}")
else:
    print("No solution found.")

