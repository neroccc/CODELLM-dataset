import json
import random
from typing import List
from functools import lru_cache

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()

        @lru_cache(None)
        def dp(end: int, event_index: int, k: int):
            if k == 0 or event_index == n:
                return 0

            event = events[event_index]
            event_start, event_end, event_value = event
            if event_start <= end:
                return dp(end, event_index + 1, k)

            attend = event_value + dp(event_end, event_index + 1, k - 1)
            skip = dp(end, event_index + 1, k)

            return max(attend, skip)

        dp.cache_clear()
        return dp(0, 0, k)


# Helper function to generate random events
def generate_random_events(num_events, max_start=10 ** 9, max_value=10 ** 6):
    events = []
    for _ in range(num_events):
        start = random.randint(1, max_start)
        end = random.randint(start, start + random.randint(1, 100))
        value = random.randint(1, max_value)
        events.append([start, end, value])
    return events


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        num_events = random.randint(1, 100)  # Keep within limits for reasonable runtime
        k = random.randint(1, num_events)
        events = generate_random_events(num_events)
        expected_output = solution.maxValue(events, k)

        test_cases.append({
            "input": {"events": events, "k": k},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1751.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
