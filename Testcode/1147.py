import json
import random
import string


class Solution:
    def longestDecomposition(self, text: str) -> int:
        magic_prime = 32416189573
        low = 0
        high = len(text) - 1
        cur_low_hash = 0
        cur_high_hash = 0
        cur_hash_length = 0
        k = 0

        while low < high:
            cur_low_hash *= 26
            cur_low_hash += ord(text[low]) - 97
            high_char = ord(text[high]) - 97
            cur_high_hash = (high_char * pow(26, cur_hash_length, magic_prime)) + cur_high_hash
            cur_low_hash %= magic_prime
            cur_high_hash %= magic_prime
            low += 1
            high -= 1
            cur_hash_length += 1

            if cur_low_hash == cur_high_hash:
                k += 2
                cur_low_hash = 0
                cur_high_hash = 0
                cur_hash_length = 0

        if (cur_hash_length == 0 and low == high) or cur_hash_length > 0:
            k += 1

        return k


def generate_random_string(min_length=1, max_length=1000):
    """Generate a random string of lowercase English letters."""
    length = random.randint(min_length, max_length)
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def generate_test_cases(num_cases=50, max_length=1000):
    """Generate test cases for the Longest Chunked Palindrome Decomposition problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        text = generate_random_string(1, max_length)
        expected_output = solution.longestDecomposition(text)
        test_cases.append({"input": text, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": "ghiabcdefhelloadamhelloabcdefghi", "output": solution.longestDecomposition("ghiabcdefhelloadamhelloabcdefghi")},
        {"input": "merchant", "output": solution.longestDecomposition("merchant")},
        {"input": "antaprezatepzapreanta", "output": solution.longestDecomposition("antaprezatepzapreanta")},
        {"input": "a", "output": solution.longestDecomposition("a")},
        {"input": "abccba", "output": solution.longestDecomposition("abccba")},
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
    max_length = 1000
    test_cases = generate_test_cases(num_cases, max_length)
    save_test_cases("test_cases_1147.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'longest_decomposition_test_cases.json'.")
