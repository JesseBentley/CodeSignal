#Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
#Example
#For inputArray = [3, 6, -2, -5, 7, 3], the output should be
#adjacentElementsProduct(inputArray) = 21.
#7 and 3 produce the largest product.
##Input/Output
#[execution time limit] 4 seconds (py3)
#[input] array.integer inputArray
#An array of integers containing at least two elements.
#Guaranteed constraints:
#2 ≤ inputArray.length ≤ 10,
#-1000 ≤ inputArray[i] ≤ 1000.
#[output] integer
#The largest product of adjacent elements.
#[Python3] Syntax Tips
#Prints help message to the console
#Returns a string

#Solution

def adjacentElementsProduct(inputArray):
    prev = inputArray[0]
    prod = prev * inputArray[1]
    for i in inputArray[1::]:
        if prev * i > prod:
            prod = prev * i
        prev = i
    return prod
