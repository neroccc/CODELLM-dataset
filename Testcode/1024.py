import json
import random
from collections import deque
from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips = deque(sorted(clips, key=lambda x: (x[0], -x[1])))

        t, cSet, ans = 0, set(), 0

        while clips:
            while clips and clips[0][1] <= t:
                clips.popleft()
            while clips and clips[0][0] <= t:
                cSet.add(clips.popleft()[1])

            if clips and not cSet:
                return -1
            t = max(cSet, default=t)
            ans += 1
            if t >= time:
                return ans
            cSet.clear()

        return -1


def generate_random_clips(max_length=100, max_time=100):
    """Generate a random set of video clips."""
    num_clips = random.randint(1, max_length)
    clips = []
    for _ in range(num_clips):
        start = random.randint(0, max_time)
        end = random.randint(start, max_time)
        clips.append([start, end])
    return clips


def generate_test_cases(num_cases=50, max_length=100, max_time=100):
    """Generate test cases for the Video Stitching problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        clips = generate_random_clips(max_length, max_time)
        time = random.randint(1, max_time)
        expected_output = solution.videoStitching(clips, time)
        test_cases.append({"input": {"clips": clips, "time": time}, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": {"clips": [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], "time": 10},
         "output": solution.videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10)},
        {"input": {"clips": [[0, 1], [1, 2]], "time": 5},
         "output": solution.videoStitching([[0, 1], [1, 2]], 5)},
        {"input": {"clips": [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]], "time": 9},
         "output": solution.videoStitching([[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]], 9)},
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
    max_length = 100
    max_time = 100
    test_cases = generate_test_cases(num_cases, max_length, max_time)
    save_test_cases("../test_cases_1024.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'video_stitching_test_cases.json'.")
