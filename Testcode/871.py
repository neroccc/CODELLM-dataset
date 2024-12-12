import json
import random
from heapq import heappush, heappop
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        fuel, heap, count = startFuel, [], 0
        stations.append([target, 0])  # Handle the case where there are no stations

        while stations:
            if fuel >= target:
                return count

            while stations and stations[0][0] <= fuel:
                _, liters = stations.pop(0)
                heappush(heap, -liters)

            if not heap:
                return -1  # Unable to reach the target
            fuel += -heappop(heap)

            count += 1


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random target and startFuel
        target = random.randint(1, 10**4)
        startFuel = random.randint(1, target)
        # Generate a random number of stations
        num_stations = random.randint(0, 50)  # Up to 50 stations for practical limits
        # Generate station positions and fuel
        stations = []
        current_position = 0
        for _ in range(num_stations):
            # Ensure a valid range for the station position
            if current_position + 1 >= target - 1:
                break  # No more valid positions for stations
            position = random.randint(current_position + 1, target - 1)
            fuel = random.randint(1, 10**4)
            stations.append([position, fuel])
            current_position = position
        # Sort stations by position to simulate realistic input
        stations.sort()

        # Compute the output using the solution's method
        output = solution.minRefuelStops(target, startFuel, stations)
        # Append the test case
        test_cases.append({
            "input": {
                "target": target,
                "startFuel": startFuel,
                "stations": stations
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_871.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
