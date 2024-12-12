import json
import random
from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)

        def fn(i):
            nonlocal ans
            if i == len(jobs):
                ans = min(ans, max(time))
            else:
                for kk in range(k):
                    if not kk or time[kk - 1] > time[kk]:
                        time[kk] += jobs[i]
                        if max(time) < ans:
                            fn(i + 1)
                        time[kk] -= jobs[i]

        ans = float('inf')
        time = [0] * k
        fn(0)
        return ans


# Helper function to generate random jobs array
def generate_random_jobs(length, max_time=10 ** 7):
    return [random.randint(1, max_time) for _ in range(length)]


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        jobs_length = random.randint(1, 12)
        k = random.randint(1, jobs_length)
        jobs = generate_random_jobs(jobs_length, max_time=10 ** 7)
        expected_output = solution.minimumTimeRequired(jobs, k)

        test_cases.append({
            "input": {"jobs": jobs, "k": k},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1723.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
