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

def get_factors(x, b):
    ans = set()
    for i in range(1, int(sqrt(x))+1):
        if x%i==0:
            ans.add(i*b)
            ans.add((x//i)*b)
    
    return ans

def process(arr, n = 1):
    curr = 1
    gg = arr[0][-1]
    hold = 1
    done = 0
    for a,b,c in arr:
        hold = hold*b//gcd(hold,b)
        gg = gcd(gg, c)

        if gg%hold==0: continue
        curr+=1
        hold = b
        gg = c
    
    return curr

        

    C = ddc(int)
    
    for a,b,c in arr:
        #print(a,b, get_factors(a,b))
        done += 1
        freq = 1
        for ele in get_factors(a,b):
            C[ele]+=1
            freq = max(freq,C[ele])
        if freq==done:
            continue
        else:
            #print('yes')
            done = 1
            curr+=1
            C.clear()
            for ele in get_factors(a,b):
                C[ele]+=1
    
    return curr

        
        
def main():
    #T-testcases

    for _ in range(intin()):
        n = intin()
        arr = []
        for i in range(n):
            a,b = mapin()
            arr.append([a,b,a*b])
        
        #arr = input()
        ans = process(arr, n)
        print(ans)
        #print("Case #{0}: {1}".format(_+1, ans))
    

#----------------------------------------------

if __name__ == "__main__":
    main()