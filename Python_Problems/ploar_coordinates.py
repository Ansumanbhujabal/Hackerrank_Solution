# Enter your code here. Read input from STDIN. Print output to STDOUT
# Input Format

# A single line containing the complex number . Note: complex() function can be used in python to convert the input as a complex number.

# Constraints

# Given number is a valid complex number

# Output Format

# Output two lines:
# The first line should contain the value of .
# The second line should contain the value of .
import cmath
n=input()
s=complex(n)
print(abs(s))
print(cmath.phase(s))
