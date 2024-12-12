import json
import random
import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        minPQ = []

        # Initialize the priority queue with the first prime multiples
        for prime in primes:
            heapq.heappush(minPQ, (prime, 0, prime))  # (value, index in output, prime factor)

        output = [1]  # The first super ugly number is always 1

        while len(output) < n:
            value, idx, prime = heapq.heappop(minPQ)

            # Avoid adding duplicate values to the output list
            if value != output[-1]:
                output.append(value)

            # Generate the next multiple of the current prime
            heapq.heappush(minPQ, (output[idx + 1] * prime, idx + 1, prime))

        return output[n - 1]


def generate_random_primes(length: int, value_range=(2, 1000)) -> List[int]:
    """
    Generates a random list of prime numbers.

    :param length: Number of primes to generate.
    :param value_range: Range of values for primes.
    :return: List of prime numbers.
    """

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    while len(primes) < length:
        candidate = random.randint(value_range[0], value_range[1])
        if is_prime(candidate) and candidate not in primes:
            primes.append(candidate)

    return sorted(primes)


def generate_test_cases(num_cases=100, max_n=1000, max_primes_length=100, value_range=(2, 1000)):
    """
    Generates test cases for the nthSuperUglyNumber function.

    :param num_cases: Number of test cases to generate.
    :param max_n: Maximum value for n.
    :param max_primes_length: Maximum number of primes.
    :param value_range: Range of prime values.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(1, max_n)
        primes_length = random.randint(1, max_primes_length)
        primes = generate_random_primes(primes_length, value_range)

        # Calculate the expected output using the provided solution
        expected_output = solution.nthSuperUglyNumber(n, primes)

        # Add test case
        test_cases.append({
            "input": {"n": n, "primes": primes},
            "output": expected_output
        })

    return test_cases


def save_test_cases_to_file(test_cases, filename="test_cases_313.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)


if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_n=1000, max_primes_length=10, value_range=(2, 50))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
