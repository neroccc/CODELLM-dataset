import json
import random

class Solution:
    def bestTeamScore(self, scores, ages):
        dp = [0] * (1 + max(ages))
        score_age = sorted(zip(scores, ages))
        for score, age in score_age:
            dp[age] = score + max(dp[:age + 1])
        return max(dp)

# Helper function to generate random test cases
def generate_test_case(num_players, max_score=10**6, max_age=1000):
    scores = [random.randint(1, max_score) for _ in range(num_players)]
    ages = [random.randint(1, max_age) for _ in range(num_players)]
    return scores, ages

# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        num_players = random.randint(1, 1000)
        scores, ages = generate_test_case(num_players)
        expected_output = solution.bestTeamScore(scores, ages)

        test_cases.append({
            "input": {"scores": scores, "ages": ages},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1626.json", "w") as f:
        json.dump(test_cases, f, indent=4)

# Generate and save the test cases
generate_test_cases()
