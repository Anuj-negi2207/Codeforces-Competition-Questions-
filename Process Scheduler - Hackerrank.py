"""
Minumum core required n processes
"""
def getMinCores(start, end):
    ans = 0
    new = [(x, 1) for x in start] + [(x+1,-1) for x in end]
    new.sort()
    
    s = 0
    for ele, x in new:
        s += x
        ans = max(ans, s)
    
    return ans

print(getMinCores([1,3,4], [3,5,6]))