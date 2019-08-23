# Given an array of strings, return another array containing all of its longest strings.

# Solution

def allLongestStrings(inputArray):
    m = max(len(s) for s in inputArray)
    r = [s for s in inputArray if len(s) == m]
    return r


