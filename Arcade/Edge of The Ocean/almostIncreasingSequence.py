# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

# Solution

def almostIncreasingSequence(sequence):
    dropped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if dropped:
                return False
            else:
                dropped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True

