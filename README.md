# Farmer, Fox, Chicken, and Seeds Problem Solver

**Author:** Abel Mendoza
**Repository:** [Farmer-Fox-Chicken-Seeds-Problem](https://github.com/abelxmendoza/Farmer-Fox-Chicken-Seeds-Problem)

## Description

This repository contains a Python script that solves the classic "Farmer, Fox, Chicken, and Seeds" problem using the Breadth-First Search (BFS) algorithm. The problem involves moving the Farmer, Fox, Chicken, and Seeds from one side of the river to the other while adhering to specific constraints:

1. The Farmer must be present for the boat to move.
2. The Fox cannot be left alone with the Chicken.
3. The Chicken cannot be left alone with the Seeds.

The script efficiently explores the state space, finds the optimal solution with the fewest moves, and ensures that constraints are not violated.

## Contents

* `BFS.py`: The Python script that implements the BFS algorithm to solve the problem. It adheres to PEP 8 guidelines and includes comments for clarity and readability.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/abelxmendoza/Farmer-Fox-Chicken-Seeds-Problem.git
```

    2. Navigate to the repository directory:

```bash
cd Farmer-Fox-Chicken-Seeds-Problem
```

    3. Run the script to solve the problem:

```bash
python3 BFS.py
```

    4. The script will output the optimal solution path or indicate that no solution 		   was found.


## Output

* If a solution is found, the script displays the sequence of states representing the steps taken to solve the problem.
* If no solution exists, it reports that no solution was found.

## Contribution

Contributions to this repository are welcome! Feel free to open issues, suggest improvements, or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.
