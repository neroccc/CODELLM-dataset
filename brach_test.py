import os
import importlib.util
import json
import sys
import time
from typing import List  # Ensure List is properly imported

# Define paths to the folders
code_folder = "python_code"  # Replace with the path to the folder containing the Python files
test_folder = "Testcase"  # Replace with the path to the folder containing the JSON test cases
output_file = "res.txt"  # Output file to save results
error_file = "error.txt"  # Output file to save errors

# Get all Python code files and test case files
code_files = sorted([f for f in os.listdir(code_folder) if f.endswith(".py")], key=lambda x: int(x.split(".")[0]))
test_files = [f for f in os.listdir(test_folder) if f.endswith(".json")]

# Open the output files
with open(output_file, "w") as res_file, open(error_file, "w") as err_file:
    # Process each pair of code and test files
    for code_file in code_files:
        try:
            start_time = time.time()

            # Extract the ID from the Python file name
            code_id = code_file.split(".")[0]  # Assumes file names are "id.py"

            # Find the corresponding test case file
            test_file = f"test_cases_{code_id}.json"
            if test_file in test_files:
                # Load the test cases
                with open(os.path.join(test_folder, test_file), "r") as tf:
                    test_cases = json.load(tf)

                # Dynamically import the Python code
                spec = importlib.util.spec_from_file_location("solution_module", os.path.join(code_folder, code_file))
                solution_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(solution_module)

                # Check if there's a class named Solution in the module
                if hasattr(solution_module, "Solution"):
                    solution_instance = solution_module.Solution()

                    # Look for callable methods inside the Solution instance
                    function_name = None
                    for attr in dir(solution_instance):
                        if callable(getattr(solution_instance, attr)) and not attr.startswith("__"):
                            function_name = attr
                            break

                    if function_name is None:
                        res_file.write(f"{code_file}: No callable method found in the Solution class.\n")
                        continue

                    # Initialize counters for this file
                    total_cases = len(test_cases)
                    passed_cases = 0

                    # Run test cases for this file
                    for case in test_cases:
                        # Check for time limit exceeded (TLE)
                        if time.time() - start_time > 30:
                            raise TimeoutError(f"TLE: {code_file} exceeded time limit of 1 minute.")

                        input_data = case["input"]
                        expected_output = case["output"]  # Adjusted to support "output" key in JSON

                        # Ensure input_data is unpacked correctly based on the function signature
                        if isinstance(input_data, dict):
                            # Handle dictionary arguments
                            result = getattr(solution_instance, function_name)(**input_data)
                        elif isinstance(input_data, list):
                            # Handle single list argument or unpack multiple arguments
                            func = getattr(solution_instance, function_name)
                            try:
                                result = func(input_data)
                            except TypeError:
                                result = func(*input_data)
                        else:
                            # Handle single arguments
                            result = getattr(solution_instance, function_name)(input_data)

                        # Compare the result with the expected output
                        if result == expected_output:
                            passed_cases += 1

                    # Calculate accuracy for this file
                    accuracy = (passed_cases / total_cases) * 100 if total_cases > 0 else 0
                    print(code_id, accuracy)
                    # Write the result to the file
                    res_file.write(f"{code_file}: {accuracy:.2f}%\n")
                else:
                    res_file.write(f"{code_file}: No Solution class found in the file.\n")
            else:
                # Write a note for missing test cases
                res_file.write(f"{code_file}: No corresponding test case file found.\n")
        except TimeoutError as e:
            err_file.write(f"{code_file}: {str(e)}\n")
            print(f"TLE in {code_file}: {str(e)}")
        except Exception as e:
            # Log other errors to the error file
            err_file.write(f"Error in {code_file}: {str(e)}\n")
            print(f"Error in {code_file}: {str(e)}")

print(f"Accuracy results saved to {output_file}.")
print(f"Errors saved to {error_file}.")
