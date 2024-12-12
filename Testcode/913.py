import json
import random
from collections import deque
from typing import List

# Constants for the game
MOUSE = 0
CAT = 1
MOUSE_WIN = 1
CAT_WIN = 2
DRAW = 0

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)

        # Initialize result map with terminal states (MOUSE_WIN/CAT_WIN)
        results = {}
        for i in range(1, n):
            results[0, i, CAT] = results[0, i, MOUSE] = MOUSE_WIN
            results[i, i, CAT] = results[i, i, MOUSE] = CAT_WIN

        # Compute outdegree for all possible states
        degree = {}
        for mouse in range(1, n):
            for cat in range(1, n):
                degree[mouse, cat, MOUSE] = len(graph[mouse])
                degree[mouse, cat, CAT] = len(graph[cat]) - int(0 in graph[cat])

        # Initialize the queue with terminal states
        q = deque([state for state in results.keys()])

        # BFS
        while q:
            mouse, cat, turn = q.popleft()
            curResult = results[mouse, cat, turn]

            # Determine previous states based on the current turn
            prevStates = []
            if turn == MOUSE:
                prevStates = [(mouse, prevCat, CAT) for prevCat in graph[cat]]
            else:
                prevStates = [(prevMouse, cat, MOUSE) for prevMouse in graph[mouse]]

            # Update previous states based on the current state's result
            for prevState in prevStates:
                if prevState in results:
                    continue
                prevMouse, prevCat, prevTurn = prevState
                if prevCat == 0:
                    continue

                degree[prevState] -= 1
                isMoverWinner = ((curResult == MOUSE_WIN and prevTurn == MOUSE) or
                                 (curResult == CAT_WIN and prevTurn == CAT))
                if isMoverWinner or degree[prevState] == 0:
                    results[prevState] = curResult
                    q.append(prevState)

        return results.get((1, 2, MOUSE), DRAW)


def generate_test_cases(num_cases=10):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Generate a random graph
        n = random.randint(3, 10)  # Limit size for practical computation
        graph = []
        for i in range(n):
            # Each node connects to a random set of other nodes
            neighbors = random.sample(range(n), random.randint(1, n - 1))
            if i in neighbors:
                neighbors.remove(i)  # No self-loops
            graph.append(neighbors)

        # Compute the result using the solution
        output = solution.catMouseGame(graph)

        # Append the test case
        test_cases.append({
            "input": {
                "graph": graph
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_913.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
