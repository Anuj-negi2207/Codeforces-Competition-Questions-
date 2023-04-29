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

def process(arr, n, k, C, D):
    ans = n
    Major = ddc(int)
    Done = set()
    for i in range(k):

        for j in range(n):
            if arr[j][i]!=arr[0][i]:
                Done.add(j)
                
    
    
    return ans - len(Done)




            
        
        
def main():
    #T-testcases

    for _ in range(intin()):
        n, k = mapin()
        arr = []
        C = ddc(int)
        D = ddc(int)
        for i in range(n):
            temp = input()
            arr.append(temp)
            for j in range(k):
                if temp[j]=='+':
                    C[j]+=1
                else:
                    D[j]+=1
        
        #arr = input()
        ans = process(arr, n, k, C, D)
        print(ans)
        #print("Case #{0}: {1}".format(_+1, ans))
    

#----------------------------------------------

if __name__ == "__main__":
    main()