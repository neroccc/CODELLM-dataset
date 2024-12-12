import json
import random
class Solution:
    MOD = 10**9 + 7

    def knightDialer(self, n: int) -> int:
        # Initialize an array to store the possible positions of the knight on the phone pad
        cur_pos = [1] * 10

        # Loop through the number of jumps required
        for jump in range(2, n + 1):
            # Create a new list to store the updated positions after each jump
            new_pos = [0] * 10

            # Calculate the new positions based on the valid knight moves
            new_pos[0] = (cur_pos[6] + cur_pos[4]) % self.MOD
            new_pos[1] = (cur_pos[6] + cur_pos[8]) % self.MOD
            new_pos[2] = (cur_pos[7] + cur_pos[9]) % self.MOD
            new_pos[3] = (cur_pos[4] + cur_pos[8]) % self.MOD
            new_pos[4] = (cur_pos[0] + cur_pos[3] + cur_pos[9]) % self.MOD
            new_pos[5] = 0  # Knight cannot move to position 5
            new_pos[6] = (cur_pos[0] + cur_pos[1] + cur_pos[7]) % self.MOD
            new_pos[7] = (cur_pos[2] + cur_pos[6]) % self.MOD
            new_pos[8] = (cur_pos[1] + cur_pos[3]) % self.MOD
            new_pos[9] = (cur_pos[2] + cur_pos[4]) % self.MOD

            # Update the current positions list for the next iteration
            cur_pos = new_pos

        # Calculate the total count of distinct phone numbers
        total_count = sum(cur_pos) % self.MOD

        return total_count

# Test case generation
def generate_knight_dialer_cases(num_cases=100, max_n=5000):
    """Generate test cases for the Knight Dialer problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(1, max_n)  # Generate random n between 1 and max_n
        expected_output = solution.knightDialer(n)  # Compute the expected output
        test_cases.append({"input": n, "output": expected_output})

    return test_cases

def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=4)

# Generate and save test cases
if __name__ == "__main__":
    num_cases = 100
    max_n = 5000  # Max value of n
    test_cases = generate_knight_dialer_cases(num_cases, max_n)
    save_test_cases("test_cases_935.json", test_cases)
    print(f"Generated {num_cases} test cases for Knight Dialer and saved to 'knight_dialer_test_cases.json'.")
