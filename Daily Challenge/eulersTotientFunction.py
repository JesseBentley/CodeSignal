# Given an integer n, find the value of phi(n), where phi is Euler's totient function.

# Example

# For n = 5, the output should be
# eulersTotientFunction(n) = 4.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer n

# Guaranteed constraints:
# 1 ≤ n ≤ 70.

# [output] integer

# Solution

from fractions import gcd
def eulersTotientFunction(n):
    l=[i for i in range(1,n+1) if i<=n and gcd(n,i)==1]
    return len(l)

