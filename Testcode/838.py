import json
import random


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        temp = ''

        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')  # Temporarily replace 'R.L' with a placeholder
            dominoes = dominoes.replace('R.', 'RR')  # Replace 'R.' with 'RR'
            dominoes = dominoes.replace('.L', 'LL')  # Replace '.L' with 'LL'

        return dominoes.replace('xxx', 'R.L')  # Restore 'R.L'


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random length for the dominoes string
        length = random.randint(1, 1000)  # Reduced length for practical computation
        # Generate a random dominoes string of given length
        dominoes = ''.join(random.choices(['L', 'R', '.'], k=length))
        # Compute the output using the solution's method
        output = solution.pushDominoes(dominoes)
        # Append the test case
        test_cases.append({
            "input": {
                "dominoes": dominoes
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_838.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
