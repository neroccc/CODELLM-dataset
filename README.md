#CODELLM-dataset

extracted_code.py extracts Python code for a specific class (class Solution:) from a text string up to a defined stop phrase, corrects its indentation, and saves it as a .py file with the necessary imports.
brach_test.py evaluates Python solution files against corresponding JSON test cases by dynamically importing each solution, executing its method, comparing outputs, and logging accuracy and errors.
Code_problem.json contains 2,000 LeetCode problems.
dp.jsonl and greedy.jsonl contain dynamic programming and greedy algorithm problems from LeetCode, respectively.
The testcase folder holds randomly generated test cases, Testcode contains the code used to generate them, and baseline records the performance of various LLMs.
