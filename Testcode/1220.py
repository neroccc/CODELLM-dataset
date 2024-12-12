import json
import random


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(1, n):
            a_next = e
            e_next = (a + i) % MOD
            i_next = (a + e + o + u) % MOD
            o_next = (i + u) % MOD
            u_next = a

            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next

        return (a + e + i + o + u) % MOD


def generate_test_cases(num_cases=50, max_n=20000):
    """Generate test cases for the Count Vowel Permutation problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(1, max_n)
        expected_output = solution.countVowelPermutation(n)
        test_cases.append({"input": n, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": 1, "output": solution.countVowelPermutation(1)},
        {"input": 2, "output": solution.countVowelPermutation(2)},
        {"input": 5, "output": solution.countVowelPermutation(5)},
        {"input": 100, "output": solution.countVowelPermutation(100)},
        {"input": 20000, "output": solution.countVowelPermutation(20000)},
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
    max_n = 20000
    test_cases = generate_test_cases(num_cases, max_n)
    save_test_cases("../test_cases_1220.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'count_vowel_permutation_test_cases.json'.")
