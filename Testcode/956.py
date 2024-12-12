import json
import random

class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        def diff_h(rods: list[int]) -> dict[int, int]:
            dh = {0: 0}
            for rod in rods:
                for d, h in list(dh.items()):
                    dh[d + rod] = max(dh.get(d + rod, 0), h)
                    dh[abs(d - rod)] = max(dh.get(abs(d - rod), 0), h + min(d, rod))
            return dh

        d1, d2 = diff_h(rods[: len(rods) // 2]), diff_h(rods[len(rods) // 2 :])
        return max(v1 + d2[k1] + k1 for k1, v1 in d1.items() if k1 in d2)

def generate_random_rods(max_length=20, max_rod_length=1000, max_sum=5000):
    """Generate a random list of rods with constraints."""
    rods = []
    while sum(rods) < max_sum and len(rods) < max_length:
        rods.append(random.randint(1, max_rod_length))
    return rods

def generate_test_cases(num_cases=50, max_length=20, max_rod_length=1000, max_sum=5000):
    """Generate test cases for the Tallest Billboard problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        rods = generate_random_rods(max_length, max_rod_length, max_sum)
        expected_output = solution.tallestBillboard(rods)
        test_cases.append({"input": rods, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": [1, 2, 3, 6], "output": solution.tallestBillboard([1, 2, 3, 6])},
        {"input": [1, 2, 3, 4, 5, 6], "output": solution.tallestBillboard([1, 2, 3, 4, 5, 6])},
        {"input": [1, 2], "output": solution.tallestBillboard([1, 2])},
    ]
    test_cases.extend(predefined_cases)

    return test_cases

def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=4)

# Generate and save test cases
if __name__ == "__main__":
    num_cases = 100
    test_cases = generate_test_cases(num_cases)
    save_test_cases("test_cases_956.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'tallest_billboard_test_cases.json'.")
