# After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, 
# and some of them are free, but there's 
# a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, 
# they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

# Solution

def matrixElementsSum(matrix):
    total = 0;
    for j in range(0, len(matrix[0])):
        for i in range(0, len(matrix)):
            if( matrix[i][j] == 0):
                break
            else:
                total += matrix[i][j]
return total

