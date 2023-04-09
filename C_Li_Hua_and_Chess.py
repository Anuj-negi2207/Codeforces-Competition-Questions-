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
#def input(): return into().decode().strip()

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

def process(n, m):
    #ask = [[0, 0], [0, m-1], [n-1, 0]]
    #get = []
    
    x,y = 0, 0
    print("?", x+1, y+1, flush=True)
    t = intin()
    
    if t<m:
        x,y = 0, t
        print("?", x+1, y+1, flush=True)
        newt = intin()
        if newt==t:
            x,y = t, 0
            print("?", x+1, y+1, flush=True)
            y = intin()
        else:
            x,y = newt, t
        
        
        #return [x, y]
    else:
        x,y = t, 0
        print("?", x+1, y+1, flush=True)
        y = intin()
        
        
    return [x, y]
        
def main():
    #T-testcases

    for _ in range(intin()):
        n, m = mapin()
        #arr = input()
        ans = process(n, m)
        print("!", ans[0]+1, ans[1]+1, flush=True)
        #print("Case #{0}: {1}".format(_+1, ans))
    

#----------------------------------------------

if __name__ == "__main__":
    main()