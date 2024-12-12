import json
import random


class Solution:
    MOD = 1000000007

    def helper(self, locations, city, finish, remainFuel, memo):
        if remainFuel < 0:
            return 0

        if memo[city][remainFuel] is not None:
            return memo[city][remainFuel]

        total = 1 if city == finish else 0

        for nextCity in range(len(locations)):
            if nextCity != city and remainFuel >= abs(locations[nextCity] - locations[city]):
                total = (total + self.helper(locations, nextCity, finish,
                                             remainFuel - abs(locations[nextCity] - locations[city]), memo)) % self.MOD

        memo[city][remainFuel] = total
        return total

    def countRoutes(self, locations, start, finish, fuel):
        n = len(locations)
        memo = [[None] * (fuel + 1) for _ in range(n)]
        return self.helper(locations, start, finish, fuel, memo)


# Helper function to generate random locations
def generate_locations(num_cities, max_distance=10 ** 9):
    return sorted(random.sample(range(1, max_distance + 1), num_cities))


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        num_cities = random.randint(2, 100)
        locations = generate_locations(num_cities)
        start = random.randint(0, num_cities - 1)
        finish = random.randint(0, num_cities - 1)
        fuel = random.randint(1, 200)

        # Compute expected output using the provided solution
        expected_output = solution.countRoutes(locations, start, finish, fuel)

        test_cases.append({
            "input": {"locations": locations, "start": start, "finish": finish, "fuel": fuel},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1575.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
