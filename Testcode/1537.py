import json
import random


class Solution:
    def maxSum(self, nums1, nums2):
        p1, p2, sum1, sum2, result = 0, 0, 0, 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                result += max(sum1, sum2) + nums1[p1]
                sum1, sum2 = 0, 0
                p1, p2 = p1 + 1, p2 + 1
            elif nums1[p1] < nums2[p2]:
                sum1 += nums1[p1]
                p1 += 1
            else:
                sum2 += nums2[p2]
                p2 += 1

        while p1 < len(nums1):
            sum1 += nums1[p1]
            p1 += 1

        while p2 < len(nums2):
            sum2 += nums2[p2]
            p2 += 1

        return (result + max(sum1, sum2)) % (10 ** 9 + 7)


# Helper function to generate strictly increasing arrays
def generate_strictly_increasing_array(length, start=1, max_step=10 ** 7):
    arr = []
    current = start
    for _ in range(length):
        current += random.randint(1, max_step // length)
        arr.append(current)
    return arr


# Generate test cases
def generate_test_cases(num_cases=10):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length1 = random.randint(1, 10 ** 5)
        length2 = random.randint(1, 10 ** 5)

        nums1 = generate_strictly_increasing_array(length1)
        nums2 = generate_strictly_increasing_array(length2)

        # Compute expected output using the provided solution
        expected_output = solution.maxSum(nums1, nums2)

        test_cases.append({
            "input": {"nums1": nums1, "nums2": nums2},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1537.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
