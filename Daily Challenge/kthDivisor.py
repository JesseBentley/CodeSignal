# Given integers n and k, find the kth divisor (1-based) of n or determine if n has less than k divisors.
# Example
# For n = 63 and k = 4, the output should be
# kthDivisor(n, k) = 9.
# Divisors of number 63 are the following: 1, 3, 7, 9, 21, 63.
# For n = 5 and k = 3, the output should be
# kthDivisor(n, k) = -1.
# Number 5 has only two divisors.
# Input/Output
# [execution time limit] 4 seconds (py3)
# [input] integer n
# Guaranteed constraints:
# 5 ≤ n ≤ 250.
# [input] integer k
# Guaranteed constraints:
# 1 ≤ k ≤ 10.
# [output] integer
# The kth divisor of n or -1 if n has less than k divisors.

# Solution

def kthDivisor(n, k):
    n = [i for i in range(1, n + 1) if n % i == 0]
    return -1 if len(n) < k else n[k - 1]