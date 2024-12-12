import json


class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        start = {}
        s1_round, s2_round, s2_idx = 0, 0, 0
        while s1_round < n1:
            s1_round += 1
            for ch in s1:
                if ch == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == len(s2):
                        s2_round += 1
                        s2_idx = 0
            if s2_idx in start:
                prev_s1_round, prev_s2_round = start[s2_idx]
                circle_s1_round, circle_s2_round = s1_round - prev_s1_round, s2_round - prev_s2_round
                result = (n1 - prev_s1_round) // circle_s1_round * circle_s2_round
                left_s1_round = (n1 - prev_s1_round) % circle_s1_round + prev_s1_round
                for key in start:
                    val = start[key]
                    if val[0] == left_s1_round:
                        result += val[1]
                        break
                return result // n2
            else:
                start[s2_idx] = (s1_round, s2_round)
        return s2_round // n2


def generate_test_cases(solution, num_cases=100):
    test_cases = []
    import random
    import string

    for _ in range(num_cases):
        # Generate random strings s1 and s2
        s1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 100)))
        s2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 100)))

        # Generate n1 and n2
        n1 = random.randint(1, 1000)  # Smaller range for efficient computation
        n2 = random.randint(1, 1000)

        test_case = {
            "s1": s1,
            "n1": n1,
            "s2": s2,
            "n2": n2
        }
        expected_output = solution.getMaxRepetitions(s1, n1, s2, n2)
        test_cases.append({
            "input": test_case,
            "output": expected_output
        })

    return test_cases


# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=1000)

# Save the test cases to a JSON file
file_path = "../test_cases_466.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
