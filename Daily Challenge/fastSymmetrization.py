# You are given a rectangular array of characters, where each symbol '*' can either be replaced with any character or left unchanged, whereas all other elements cannot be changed. Y
# ou would like to make the minimum possible number of replacements to make the array symmetric with respect to both the horizontal and vertical middle axes, 
# i.e.  such an array that looks the same when flipped horizontally or vertically.
# Given array a, return the resulting symmetric array. If this symmetry is impossible to obtain, return an empty 2D array instead.
# Example
# For
# a = [['*', '*', 'c', '*'],
#      ['*', 'b', '*', 'a'],
#      ['a', '*', '*', '*'],
#      ['*', '*', 'c', '*']]
# the output should be
# fastSymmetrization(a) = [['*', 'c', 'c', '*'],
#                          ['a', 'b', 'b', 'a'],
#                          ['a', 'b', 'b', 'a'],
#                          ['*', 'c', 'c', '*']]
# For
# a = [['*', 'a', 'b', '*'],
#      ['*', 'a', 'b', '*']]
# the output should be
# fastSymmetrization(a) = []
# Since only asterisks can be changed, symmetry along the vertical axis is impossible to obtain.
# Input/Output
# [execution time limit] 4 seconds (py3)
# [input] array.array.char a
# Rectangular array of characters with even numbers of rows and columns.
# Guaranteed constraints:
# 2 ≤ a.length ≤ 20,
# 2 ≤ a[i].length ≤ 20.
# [output] array.array.char

def fastSymmetrization(a):
  n = len(a)
  m = len(a[0])
  for i in range(n):
    for j in range(m):
      s = {a[i][j], a[i][m-j-1], a[n-i-1][j], a[n-i-1][m-j-1]}
      if len(s) != 1:
        s.discard("*")
        if len(s) != 1:
          return []
        a[i][j] = a[i][m-j-1] = a[n-i-1][j] = a[n-i-1][m-j-1] = s.pop()
  return a
