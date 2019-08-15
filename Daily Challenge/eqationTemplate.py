def equationTemplate(v):
    from itertools import permutations
    for p in list(permutations(v)):
        if p[0]*p[1] == p[2]*p[3] or p[0] == p[1]*p[2]*p[3]:
            return True
    return False