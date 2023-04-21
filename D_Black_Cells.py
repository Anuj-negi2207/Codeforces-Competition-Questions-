""" THIS TEMPLATE belongs to anuj_negi || Updated - 5th Feb """

""" Use sortedcontainers, Multiset when available """
""" 'bisect' for binary search and insertion """
import io,os
from bisect import *
from heapq import *
from math import *
from collections import defaultdict as ddc, Counter, deque
from functools import *
from itertools import *
from sys import setrecursionlimit
#from functools import cache, lru_cache
#from typing import Generic, Iterable, Iterator, TypeVar, Union, List
#T = TypeVar('T')


into = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return into().decode().strip()

def intin(): return int(input())
def mapin(): return list(map(int, input().split()))

#----------------------------------------------

INF = 1<<64             #Or use 10**20
mod = 1_000_000_007     #Or 998_244_353
yes = "YES"
no = "NO"
even = "EVEN"
odd = "ODD"
alice = "ALICE"
bob = "BOB"


#----------------------------------------------

"""
SOME FACTS THAT CAN BE USED LATER - 

->  if n is prime, then -> (a**(n-1)) % n = 1

->  When cases like DEFICIENT CITY to SURPLUS CITY, work on BFS using SURPLUS city and check for DEFICIENT city

->  PALINDROMEs and str-len FACTORS have some relations. if P = XQ where P, X, Q are palindromes, then X have the possible length in Factors of 'n'

->  When all substrings are said to be checked, we can go for 2 loops (With 100 limit of inner loop, minimize the memory)

->  Bezout's Lemma states that if x and y are nonzero integers and g = gcd(x,y), 
    then there exist integers a and b such that ax+by=g. 
    In other words, there exists a linear combination of x and y equal to g. 
"""

#----------------------------------------------

def process(arr, n, k):

    tot = sum(r-l+1 for l,r in arr)
    if tot<k: return -1
    
    Q = []

    ans = 1e18
    curr = 0
    last = 0

    for l,r in arr:
        last = r
        curr += r-l+1
        extra = max(0, curr-k)
        while Q and (extra-Q[0])>=0:
            temp = 2*(len(Q)+1) + last - (curr-k)
            ans = min(ans, temp)
            x = heappop(Q)
            curr -= x
            extra -= x
            
    
        heappush(Q, r-l+1 - max(curr-k, 0))
        #print(Q)
        if curr>=k:
            temp = 2*(len(Q)) + last - (curr-k)
            #print(l, r, curr, temp)
            curr = k
            ans = min(ans, temp)
    
    return ans

        
        
def main():
    #T-testcases

    for _ in range(intin()):
        n, k = mapin()
        L = mapin()
        R = mapin()
        arr = list(zip(L, R))
        ans = process(arr, n, k)
        print(ans)
        #print("Case #{0}: {1}".format(_+1, ans))
    

#----------------------------------------------

if __name__ == "__main__":
    main()