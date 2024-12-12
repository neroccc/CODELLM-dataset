import json
import random
import string

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1

        while s_idx < s_len:
            if p_idx < p_len and p[p_idx] in ["?", s[s_idx]]:
                s_idx += 1
                p_idx += 1
            elif p_idx < p_len and p[p_idx] == "*":
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            elif star_idx == -1:
                return False
            else:
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx

        return all(p[i] == "*" for i in range(p_idx, p_len))

def generate_random_string(length, characters):
    """
    Generates a random string of a given length from the specified characters.
    """
    return ''.join(random.choice(characters) for _ in range(length))

def generate_test_cases(num_cases=1000, max_length=50):
    """
    Generates test cases for the isMatch function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the strings and patterns.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Random string generation
        s_length = random.randint(0, max_length)
        s = generate_random_string(s_length, string.ascii_lowercase)

        # Random pattern generation
        p_length = random.randint(0, max_length)
        pattern_chars = string.ascii_lowercase + "?*"
        p = generate_random_string(p_length, pattern_chars)

        # Calculate expected output
        expected_output = solution.isMatch(s, p)

        # Add test case
        test_cases.append({
            "input": {"s": s, "p": p},
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_44.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    num_cases = 1000
    test_cases = generate_test_cases(num_cases=num_cases, max_length=50)

    # Save to file
    save_test_cases_to_file(test_cases)
    print(f"{num_cases} test cases saved to 'test_case_.json'.")
