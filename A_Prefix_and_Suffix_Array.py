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

def check(s, arr):
    curr = []
    for i in range(len(s)-1):
        curr.append(s[:i+1])
        curr.append(s[i+1:])
    #print(sorted(curr), sorted(arr))
    return sorted(curr)==sorted(arr)


def process(arr, n = 1):
        
    x,y = [ele for ele in arr if len(ele)==(n-1)]
    
    if x[1:] in y:
        t1 = x[0]+y 
        #print(x[0]+y, x+y[-1])
        if t1==t1[::-1] and check(t1, arr): return yes
    
    if y[1:] in x:
        t2 = y[0]+x
        #print(y[0]+x, y+x[-1])
        if t2==t2[::-1] and check(t2, arr): return yes

    return no
           
        
        
def main():
    #T-testcases

    for _ in range(intin()):
        n = intin()
        arr = list(input().split())
        #arr = input()
        ans = process(arr, n)
        print(ans)
        #print("Case #{0}: {1}".format(_+1, ans))
    

#----------------------------------------------

if __name__ == "__main__":
    main()