import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define the initial state
initial_state = ("L", "L", "L", "L")  # (Farmer, Fox, Chicken, Seeds) all on the left side

# Define the goal state
goal_state = ("R", "R", "R", "R")  # (Farmer, Fox, Chicken, Seeds) all on the right side

# Function to generate valid successor states
def get_successors(state):
    successors = []
    farmer, fox, chicken, seeds = state
    
    # Possible actions: F for Farmer, X for Fox, C for Chicken, S for Seeds
    actions = ["F", "FX", "FC", "FS"]
    
    for action in actions:
        new_state = list(state)
        new_farmer = "R" if farmer == "L" else "L"
        
        # Move items according to the action
        for item in action:
            if item == "F":
                new_state[0] = new_farmer
            elif item == "X":
                new_state[1] = new_farmer
            elif item == "C":
                new_state[2] = new_farmer
            elif item == "S":
                new_state[3] = new_farmer
        
        # Check if the resulting state is valid
        if (new_state[2] != new_state[1] and new_state[1] == new_state[3]) or (new_state[2] != new_state[0] and new_state[0] == new_state[3]):
            successors.append(tuple(new_state))
    
    return successors

# Generate all possible states and add them to the graph
visited_states = set()
states_to_visit = [initial_state]

while states_to_visit:
    current_state = states_to_visit.pop(0)
    G.add_node(current_state)
    visited_states.add(current_state)
    
    for successor in get_successors(current_state):
        if successor not in visited_states:
            states_to_visit.append(successor)
            G.add_edge(current_state, successor)

# Plot the state space graph
pos = nx.spring_layout(G, seed=42)
labels = {state: f"({','.join(state)})" for state in G.nodes()}

plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, labels=labels, node_size=5000, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("State Space of Farmer, Fox, Chicken, and Seeds Problem")

# Add description at the bottom of the diagram
description = (
    "The Farmer, Fox, Chicken, and Seeds problem involves moving the farmer,\n"
    "fox, chicken, and seeds from the left side of the river to the right side\n"
    "of the river. The farmer can only carry one item at a time and must ensure\n"
    "that the fox and chicken, or the chicken and seeds, are not left alone\n"
    "on either side without the farmer's presence, as the fox will eat the chicken,\n"
    "and the chicken will eat the seeds."
)
plt.gcf().text(0.1, -0.05, description, fontsize=12)

plt.show()
