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
#For Minimum Swaps to sort
def sortArrayMinSwap(arr, n):
    #O(nlogn)
    ans = 0
    Another = {ele:i for i, ele in enumerate(sorted(arr))}
    complete = [True]*n
    
    for j in range(n):
        i = j
        curr = 0
        while complete[i]:
            complete[i] = False
            i = Another[arr[i]]
            curr+=1
        
        if curr>0:
            ans += curr-1

    return ans

def change(arr, n, k, first):
    arr[0], arr[first] = arr[first], arr[0]
    for i in range(n-k):
        j = i
        nex = j+k
        while nex<n and arr[j]>arr[j+k]:
            arr[j], arr[j+k] = arr[j+k], arr[j]
            j = nex
            nex = j+k
    
    for i in range(n-1, k, -1):
        j = i
        nex = j-k
        while nex>-1 and arr[j]<arr[nex]:
            arr[j], arr[nex] = arr[nex], arr[j]
            j = nex
            nex = j-k

    if sorted(arr)==arr:
        return True
    return False

def process(arr, n, k = 1):
    arr = [0] + arr
    n+=1
    
    for i in range(n-k):
        j = i
        nex = j+k
        while nex<n and arr[j]>arr[j+k]:
            arr[j], arr[j+k] = arr[j+k], arr[j]
            j = nex
            nex = j+k
    
    for i in range(n-1, k, -1):
        j = i
        nex = j-k
        while nex>-1 and arr[j]<arr[nex]:
            arr[j], arr[nex] = arr[nex], arr[j]
            j = nex
            nex = j-k

    if sorted(arr)==arr:
        return 0
    
    print(arr)
    def find(x):
        if parent[x]!=x: parent[x] = find(parent[arr[x]])
        return parent[x]

    parent = list(range(n))
    for i in range(n):
        parent[i] = find(parent[arr[i]])

    print(parent)
    return -1
            
        
        
def main():
    #T-testcases

    for _ in range(intin()):
        n, k = mapin()
        arr = mapin()
        #arr = input()
        ans = process(arr, n, k)
        print(ans)
        #print("Case #{0}: {1}".format(_+1, ans))
    

#----------------------------------------------

if __name__ == "__main__":
    main()