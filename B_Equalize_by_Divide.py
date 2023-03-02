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

def process2(arr, n):
    x = min(arr)
    ans = []
    k = arr.index(x)

    for i in range(n):
        while arr[i]>x:
            ans.append([i, k])
            arr[i] = ceil(arr[i]/arr[k])
    
    if len(set(arr))==1:
        print(len(ans))
        for l,r in ans:
            print(l+1, r+1)
    
    else:
        print(-1)



def process(arr, n = 1):
    if len(set(arr))==1: 
        print(0)
        return

    check = arr.count(1)
    if 0<check<n:
        print(-1)
        return
    
    ans = []
    if 2 in arr:
        k = arr.index(2)

    else:
        k, l = -1, -1
        for i in range(n):
            for j in range(n):
                if i!=j:    
                    x,y = arr[i], arr[j]
                    while x>2:
                        x = ceil(x/y)
                    if x==2:
                        k, l = i, j
                        break
            
            if k!=-1: break
        
        if k==-1: 
            process2(arr, )
            return
        
        while arr[k]>2:
            ans.append([k, l])
            arr[k] = ceil(arr[k]/arr[l])
    
    for i in range(n):
        while arr[i]>2:
            ans.append([i, k])
            arr[i] = ceil(arr[i]/arr[k])
    
    #print(arr)
    print(len(ans))
    for l,r in ans:
        print(l+1, r+1)
    


        
        
def main():
    #T-testcases

    for _ in range(intin()):
        n = intin()
        arr = mapin()
        #arr = input()
        process(arr, n)
        #print("Case #{0}: {1}".format(_+1, ans))
    

#----------------------------------------------

if __name__ == "__main__":
    main()