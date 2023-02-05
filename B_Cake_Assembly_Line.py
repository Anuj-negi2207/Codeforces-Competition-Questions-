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

def check(Cake, Drip, n, w, h, change):
    
    #for change in range(left, right+1):    
    Find = [0]*n
    i,j = 0, 0
    while i<n and j<n:
        cake = Cake[i]+change
        disp = Drip[j]
        
        if (cake-w)<=(disp-h)<=(disp+h)<=(cake+w):
            Find[i] = 1
        
        if cake>disp:
            j+=1
        else:
            i+=1
    
    while i<n:
        cake = Cake[i]+change
        disp = Drip[-1]
        
        if (cake-w)<=(disp-h)<=(disp+h)<=(cake+w):
            Find[i] = 1
        i+=1
    
    while j<n:
        cake = Cake[-1]+change
        disp = Drip[j]
        
        if (cake-w)<=(disp-h)<=(disp+h)<=(cake+w):
            Find[-1] = 1

        j+=1
    
    return sum(Find)==n


    

def process(A, B, n, w, h):

    #Checking First
    left, right = [], []
    for x in range(n):
        disp, cake = B[x], A[x]
        left.append((disp-h)-(cake-w))
        right.append((disp+h)-(cake+w))
        
    """    
    for x in [0, -1]:    
        disp, cake = B[x], A[x]
        left, right = (disp-h)-(cake-w), (disp+h)-(cake+w)
        #print(left, right)"""

    if check(A, B, n, w, h, min(left)): return yes
    if check(A, B, n, w, h, min(right)): return yes
    if check(A, B, n, w, h, max(left)): return yes
    if check(A, B, n, w, h, max(right)): return yes
    
    return no   
        
        
def main():
    #T-testcases

    for _ in range(intin()):
        n,w,h = mapin()
        A = mapin()
        B = mapin()
        #arr = input()
        ans = process(A, B, n, w, h)
        print(ans)
        #print("Case #{0}: {1}".format(_+1, ans))
    

#----------------------------------------------

if __name__ == "__main__":
    main()