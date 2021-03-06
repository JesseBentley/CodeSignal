# Imagine the following situation for a given integers n and k. There are n people standing in a circle. They are numbered from 1 through n in clockwise direction. T
# he counting out begins at person #1 and continues around the circle in a clockwise direction. In each step, k-1 people are skipped and the next person is removed from the circle. 
# The elimination proceeds around the circle (which is becoming smaller and smaller as people get removed), until only one person remains, who is announced a winner.
# The task is to find the place in the initial circle that would guarantee a win.
# Example
# For n = 3 and k = 2, the output should be
# josephusProblem(n, k) = 3.
# Check out the image below for better understanding:
# Input/Output
# [execution time limit] 4 seconds (py3)
# [input] integer n
# A positive integer representing the number of people.
# Guaranteed constraints:
# 3 ≤ n ≤ 10.
# [input] integer k
# A positive integer.
# Guaranteed constraints:
# 2 ≤ k ≤ 10.
# [output] integer
# The index of the winning place.

# Solution

def josephusProblem(n, k):
    if n == 1:
        return 1
    return 1 + (josephusProblem(n-1, k) + k-  1) % n