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


def process(arr, n = 1):
    #defaultdict consumes more time
    C = [{} for i in range(26)]
    mask = (1<<26) - 1
    ans = 0

    for s in arr:
        D = [0]*26
        for ch in s:
            D[ord(ch)-97] += 1
        
        curr = 0
        for i in range(26):
            if D[i]%2:          #IF character is odd
                curr |= (1<<i)
        
        for i in range(26):
            if D[i]==0:
                ans += C[i].get(mask^(1<<i)^curr, 0)   #Odd length and 25 unique characters
        
        for i in range(26):
            if D[i]==0:
                C[i][curr] = C[i].get(curr, 0) + 1
    
    return ans


        
        
def main():
    #T-testcases
    n = intin()
    arr = []
    for _ in range(n):
        arr.append(input())

    ans = process(arr, n)
    print(ans)
    #print("Case #{0}: {1}".format(_+1, ans))
    

#----------------------------------------------

if __name__ == "__main__":
    main()