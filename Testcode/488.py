import json
import collections
import random


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # Helper function to remove consecutive balls
        def remove_same(s, i):
            if i < 0:
                return s

            left = right = i
            while left > 0 and s[left - 1] == s[i]:
                left -= 1
            while right + 1 < len(s) and s[right + 1] == s[i]:
                right += 1

            length = right - left + 1
            if length >= 3:
                new_s = s[:left] + s[right + 1:]
                return remove_same(new_s, left - 1)
            else:
                return s

        # Sort hand for easier processing
        hand = "".join(sorted(hand))

        # Initialize BFS queue and visited set
        q = collections.deque([(board, hand, 0)])
        visited = set([(board, hand)])

        while q:
            curr_board, curr_hand, step = q.popleft()
            for i in range(len(curr_board) + 1):
                for j in range(len(curr_hand)):
                    if j > 0 and curr_hand[j] == curr_hand[j - 1]:
                        continue
                    if i > 0 and curr_board[i - 1] == curr_hand[j]:
                        continue
                    pick = False
                    if i < len(curr_board) and curr_board[i] == curr_hand[j]:
                        pick = True
                    if 0 < i < len(curr_board) and curr_board[i - 1] == curr_board[i] and curr_board[i] != curr_hand[j]:
                        pick = True
                    if pick:
                        new_board = remove_same(curr_board[:i] + curr_hand[j] + curr_board[i:], i)
                        new_hand = curr_hand[:j] + curr_hand[j + 1:]
                        if not new_board:
                            return step + 1
                        if (new_board, new_hand) not in visited:
                            q.append((new_board, new_hand, step + 1))
                            visited.add((new_board, new_hand))
        return -1


def generate_test_cases(solution, num_cases=100):
    test_cases = []
    colors = ['R', 'Y', 'B', 'G', 'W']

    for _ in range(num_cases):
        # Generate a random board with length between 1 and 16
        board_length = random.randint(1, 16)
        board = ''.join(random.choices(colors, k=board_length))

        # Generate a random hand with length between 1 and 5
        hand_length = random.randint(1, 5)
        hand = ''.join(random.choices(colors, k=hand_length))

        # Calculate expected output using the provided solution
        expected_output = solution.findMinStep(board, hand)

        # Add test case
        test_cases.append({
            "input": {"board": board, "hand": hand},
            "output": expected_output
        })

    return test_cases


# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=1000)

# Save the test cases to a JSON file
file_path = "../test_cases_488.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
