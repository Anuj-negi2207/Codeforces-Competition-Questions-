"""THIS TEMPLATE belongs to anuj_negi"""

#Try to use bisect in case of binary search, bisect_left, bisect_right
#Try to use sortedcontainers when available
#Try to use Multiset when available
from bisect import *
from heapq import *
#from functools import cache, lru_cache
from math import *
from collections import defaultdict as ddc
from collections import Counter
from functools import *
from itertools import *
from sys import setrecursionlimit
import io,os

into = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return into().decode().strip()

def intin(): return int(input())
def mapin(): return list(map(int, input().split()))
def strin(): return input().split()   
def graphin(m):
    zz = ddc(set)
    for i in range(m):
        a, b = mapin()
        zz[a].add(b)
        zz[b].add(a)
    
    return zz

#----------------------------------------------

INF = 1<<64     #Or use 10**20
mod = 10**9 + 7
yes = "YES"
no = "NO"
even = "EVEN"
odd = "ODD"
alice = "ALICE"
bob = "BOB"

#----------------------------------------------
#Starts from here

def sortArrayMinSwap(arr, n):
    #O(nlogn)
    ans = 0
    Another = {ele:i for i, ele in enumerate(sorted(arr))}
    Another2 = ddc(int)
    complete = [True]*n
    
    for j in range(n):
        i = j
        curr = 0
        #Another2[arr[i]] = j
        while complete[i]:
            #print(i)
            Another2[arr[i]] = j
            complete[i] = False
            i = Another[arr[i]]
            #Another2[i] = j
             
            curr+=1
        if curr>0:
            ans += curr-1
    
    #print(Another2)
    
    for i in range(n-1):
        x, y = arr[i], arr[i+1]
        if Another2[x]==Another2[y]:
            ans -= 2
            break

    return ans+1

#----------------------------------------------
def main():
    #T-testcases
    for _ in range(int(input())):
        n = intin()
        #graph = graphin(n)
        arr = mapin()
        ans = sortArrayMinSwap(arr,n)
        print(ans)
        #print("Case #{0}: {1}".format(_+1, ans))


#----------------------------------------------


if __name__ == "__main__":
    main()