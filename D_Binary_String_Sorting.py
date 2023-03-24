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

swap, delete = 10**12, 10**12 + 1


def process(arr):
    n = len(arr)
    if n==1: return 0
    ans = 10**18
    zero, one = 0, arr.count('1')

    for i in range(n-1):
        if arr[i] == '0':
            zero+=1
        else:
            one-=1
        temp = zero+one + (arr[i]=='1') + (arr[i+1]=='0')
        curr = (n-temp)*delete

        if arr[i]>arr[i+1]: curr += swap
        ans = min(ans, curr)
    
    return ans


    if arr.count('1') in [0, n]: return 0

    one = 0
    pref = [0]*(n+1)

    for i in range(n):
        if arr[i] == '0':
            pref[i+1] = min(one, pref[i]+1)
        else:
            one+=1
            pref[i+1] = pref[i]

    ans = pref[n]*delete
    
    zero = arr.count('0')
    curr = 0
    one = 0
    swapped = 0
    for i in range(n):
        if arr[i]=='0':
            zero-=1
            swapped += one
            
        else:
            one+=1
        
        curr = swapped*swap + zero*delete
        ans = min(ans, curr)
    
    curr = 0
    one = arr.count('1')
    zero = 0
    swapped = 0

    for i in range(n-1, -1, -1):
        if arr[i]=='1':
            one-=1
            swapped += zero
            
        else:
            zero+=1
        
        curr = curr = swapped*swap + one*delete
        ans = min(ans, curr)
    
    return ans
        
        
def main():
    #T-testcases

    for _ in range(intin()):
        arr = input()
        #arr = input()
        ans = process(arr)
        print(ans)
        #print("Case #{0}: {1}".format(_+1, ans))
    

#----------------------------------------------

if __name__ == "__main__":
    main()