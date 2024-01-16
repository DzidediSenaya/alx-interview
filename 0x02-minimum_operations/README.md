Minimum Operations

Requirements
All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
All files should end with a new line.
The first line of all files should be exactly #!/usr/bin/python3.
A README.md file at the root of the project folder is mandatory.
Code documentation is required.
Code should adhere to the PEP 8 style (version 1.7.x).

All files must be executable.
Task
0. Minimum Operations
In the text file, there is initially a single character 'H.' The text editor can execute two operations: Copy All and Paste. The task is to write a method minOperations(n) that calculates the fewest number of operations needed to result in exactly n 'H' characters in the file.

Prototype
python
Copy code
def minOperations(n)
Returns
An integer representing the minimum number of operations.
Example
python
Copy code
n = 9

# Operations:
# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHH => Paste => HHHHHHHHH
# Number of operations: 6
result = minOperations(n)
print("Number of operations:", result)
Usage
To test the script, you can use the provided 0-main.py file. Execute it in the terminal:
