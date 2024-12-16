import re

def extract_all_code_from_string(input_string, class_name="class Solution:", stop_phrase="# Problem Description3"):
    lines = input_string.splitlines()
    extracted_code = []
    capturing = False
    class_indent = None
    current_method_indent = None
    inside_method = False

    for line in lines:
        # Stop if the stop phrase is found
        if stop_phrase in line:
            break

        # Check for class start
        if line.strip().startswith(class_name):
            capturing = True
            class_indent = len(line) - len(line.lstrip())
            extracted_code.append(line)
            continue

        if capturing:
            indent_level = len(line) - len(line.lstrip())
            stripped = line.strip()

            # If empty line, it can be part of code
            if stripped == "":
                extracted_code.append(line)
                continue

            # If we are not inside a method yet, look for a method definition
            if not inside_method:
                if indent_level > class_indent and stripped.startswith("def "):
                    # Found a method definition
                    inside_method = True
                    current_method_indent = indent_level
                    extracted_code.append(line)
                elif indent_level > class_indent and (stripped.startswith("class ") or stripped.startswith("def ")):
                    # Another class or method at the class level
                    extracted_code.append(line)
                else:
                    # If we find something at or beyond class indent that's not a method/class definition,
                    # it means we are seeing non-code lines after class definition.
                    break
            else:
                # We are currently inside a method.
                if indent_level > current_method_indent:
                    # Still inside the method block
                    extracted_code.append(line)
                else:
                    # We've returned to method-level indentation or higher
                    # Check if this is another def or class (another code block at class level)
                    if stripped.startswith("def ") or stripped.startswith("class "):
                        # Another method or class at the same level, continue capturing
                        extracted_code.append(line)
                        inside_method = True
                        current_method_indent = indent_level
                    else:
                        # This line is not starting a new code block and it's at method-level indent,
                        # so it's non-code line. Stop capturing.
                        break

    if not extracted_code:
        return "No Python code was found before the stop phrase."

    return "\n".join(extracted_code)



def fix_first_line_indentation_in_string(input_code):
    """
    Fix the leading spaces in the first line of a Python code block and adjust subsequent lines accordingly.

    Args:
        input_code (str): The extracted Python code as a string.

    Returns:
        str: The Python code with fixed indentation.
    """
    lines = input_code.splitlines()
    if not lines:
        return "The input code is empty."

    # Determine the leading spaces of the first line
    first_line = lines[0]
    leading_spaces = len(first_line) - len(first_line.lstrip())

    # Remove leading spaces from all lines if the first line has unnecessary spaces
    if leading_spaces > 0:
        cleaned_lines = [line[leading_spaces:] for line in lines]
    else:
        cleaned_lines = lines

    # Return the cleaned code as a string
    return "\n".join(cleaned_lines)

def save_code_to_file(code_string, file_path):
    """
    Save a string of Python code to a .py file.

    Args:
        code_string (str): The Python code as a string.
        file_path (str): The path of the .py file to save.
    """
    with open(file_path, 'w') as file:
        file.write("from typing import List\n")
        file.write(code_string)
    print(f"Fixed code saved to {file_path}")

# Example usage
input_string = r"""
Question ID: 1976
Code Description: You are in a city that consists of `n` intersections numbered from `0` to `n - 1` with **bi-directional** roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer `n` and a 2D integer array `roads` where `roads[i] = [ui, vi, timei]` means that there is a road between intersections `ui` and `vi` that takes `timei` minutes to travel. You want to know in how many ways you can travel from intersection `0` to intersection `n - 1` in the **shortest amount of time**.

Return _the **number of ways** you can arrive at your destination in the **shortest amount of time**_. Since the answer may be large, return it **modulo** `109 + 7`.

**Example 1:**

**Input:** n = 7, roads = \[\[0,6,7\],\[0,1,2\],\[1,2,3\],\[1,3,3\],\[6,3,3\],\[3,5,1\],\[6,5,1\],\[2,5,1\],\[0,4,5\],\[4,6,2\]\]
**Output:** 4
**Explanation:** The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

**Example 2:**

**Input:** n = 2, roads = \[\[1,0,10\]\]
**Output:** 1
**Explanation:** There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.

**Constraints:**

*   `1 <= n <= 200`
*   `n - 1 <= roads.length <= n * (n - 1) / 2`
*   `roads[i].length == 3`
*   `0 <= ui, vi <= n - 1`
*   `1 <= timei <= 109`
*   `ui != vi`
*   There is at most one road connecting any two intersections.
*   You can reach any intersection from any other intersection.
Generated Code:
) / 2`
*   `0 <= ui, vi < n`
*   `ui != vi`
*   `0 <= timei <= 1000`
*   There are no duplicate roads.
*   Each intersection is reachable from any other intersection.

# Python Code
class Solution:
    def countPaths(self, n: int, roads: List[List[int]) -> int:
        MOD = 10**9 + 7
        adj_list = [[] for _ in range(n)]
        time = [float('inf')] * n
        time[0] = 0
        time[n - 1] = 0

        for u, v, t in roads:
            adj_list[u].append((v, t))
            adj_list[v].append((u, t))

        def dfs(node, prev):
            for neighbor, t in adj_list[node]:
                if neighbor != prev:
                    if time[node] + t < time[neighbor]:
                        time[neighbor] = time[node] + t
                        dfs(neighbor, node)

        dfs(0, -1)
        dfs(n - 1, -1)

        dp = [1] * n
        for i in range(n - 2, -1, -1):
            for neighbor, t in adj_list[i]:
                if time[i] + t == time[neighbor]:
                    dp[i] = (dp[i] + dp[neighbor]) % MOD

        return dp[0]
    hello
    ssss
    ssss
    # Refer to the algorithm description to generate a complete and efficient Python solution for the given Problem Description3

    # Problem Description3
    You are given a list of `n` people, `skills`, where `skills[i]` is a **bitmask** representing the skills of the ith person. Two people can communicate if and only if their skills intersect.

Return the maximum number of people you can communicate with efficiently.

**Example 1:**

**Input:** skills = [2,1,3], k = 2
**
"""

# Extract and fix the code
extracted_code = extract_all_code_from_string(input_string)
print(extracted_code)
fixed_code = fix_first_line_indentation_in_string(extracted_code)


save_code_to_file(fixed_code, 'fixed_code.py')