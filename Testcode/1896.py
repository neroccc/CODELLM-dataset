import json
import random


def generate_boolean_expression(length):
    """Generate a random valid boolean expression of a given length."""
    operators = ['&', '|']
    elements = ['0', '1'] + operators
    expression = []

    for _ in range(length):
        if len(expression) == 0 or expression[-1] in operators + ['(']:
            expression.append(random.choice(['0', '1', '(']))
        elif expression[-1] in ['0', '1']:
            if random.random() < 0.5:
                expression.append(random.choice(operators))
            else:
                if '(' in expression:
                    expression.append(')')

    # Balance parentheses
    open_count = expression.count('(')
    close_count = expression.count(')')
    expression.extend([')'] * (open_count - close_count))

    return ''.join(expression)


def generate_test_cases(num_cases=1000, max_length=100):
    """Generate a list of test cases."""
    test_cases = []
    for _ in range(num_cases):
        length = random.randint(1, max_length)
        test_cases.append(generate_boolean_expression(length))
    return test_cases


def compute_expected_outputs(test_cases):
    """Compute the expected outputs for a list of test cases."""
    solution = Solution()
    outputs = []
    for case in test_cases:
        try:
            output = solution.minOperationsToFlip(case)
            outputs.append(output)
        except Exception as e:
            outputs.append(str(e))  # Handle edge cases where input may be malformed
    return outputs


class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        loc = {}
        stack = []
        for i in reversed(range(len(expression))):
            if expression[i] == ")":
                stack.append(i)
            elif expression[i] == "(":
                loc[stack.pop()] = i

        def fn(lo, hi):
            """Return value and min op to change value."""
            if lo == hi: return int(expression[lo]), 1
            if expression[hi] == ")" and loc[hi] == lo: return fn(lo + 1, hi - 1)  # strip parenthesis
            mid = loc.get(hi, hi) - 1
            v, c = fn(mid + 1, hi)
            vv, cc = fn(lo, mid - 1)
            if expression[mid] == "|":
                val = v | vv
                if v == vv == 0:
                    chg = min(c, cc)
                elif v == vv == 1:
                    chg = 1 + min(c, cc)
                else:
                    chg = 1
            else:  # expression[k] == "&"
                val = v & vv
                if v == vv == 0:
                    chg = 1 + min(c, cc)
                elif v == vv == 1:
                    chg = min(c, cc)
                else:
                    chg = 1
            return val, chg

        return fn(0, len(expression) - 1)[1]


# Generate test cases
test_cases = generate_test_cases()

# Compute expected outputs
expected_outputs = compute_expected_outputs(test_cases)

# Save test cases and outputs to a JSON file
test_data = [{"input": case, "output": output} for case, output in zip(test_cases, expected_outputs)]

with open("test_cases_1896.json", "w") as f:
    json.dump(test_data, f, indent=4)

print("Test cases generated and saved to 'test_case_.json'")
