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
mod = 998_244_353
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
#Fast multiplication
def fastMul(a, b, mod = 10**9 + 7):
    t = 0
    while(b > 0):   

        if (b % 2 != 0):
            t = (t + a) % mod

        a = (a + a) % mod 
        b //= 2
    return t % mod


#----------------------------------------------
#Returns P*Q^-1 % Mod
def modInv(p, q=1, mod = 10**9 + 7):
    expo = 0
    expo = mod - 2
 
    while (expo):
        if (expo & 1):
            p = (p * q) % mod
        q = (q * q) % mod
        expo >>= 1
    return p

#----------------------------------------------

def process(arr, n):
    ans = 1
    for i in range(0, n, 3):
        a, b, c = sorted(arr[i:i+3])
        if a==b==c:
            ans *= 3
        elif a==b:
            ans *= 2
        ans %= mod
    
    m = n//3
    for i in range(m, m//2, -1):
        ans = ans * i
        ans%=mod
    
    #print(ans)
    
    for i in range(m//2, 1, -1):
        ans = modInv(ans, i, mod)
    
    return ans  
        
        
def main():
    #T-testcases

    n = intin()
    arr = mapin()
    #arr = input()
    ans = process(arr, n)
    print(ans)
    #print("Case #{0}: {1}".format(_+1, ans))
    

#----------------------------------------------

if __name__ == "__main__":
    main()