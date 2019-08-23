# Given array of integers, for each position i, search among the previous 
# positions for the last (from the left) position that contains a smaller value. 
# Store this value at position i in the answer. If no such value can be found, store -1 instead.

# Solution
def arrayPreviousLess(t):
    a = []
    for i in range(len(t)):
        b = -1
        for j in range(i-1, -1, -1):
            if t[i] > t[j]:
                b = t[j]
                break
        a.append(b)
    return a