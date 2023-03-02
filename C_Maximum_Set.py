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
N = 10**6
"""factors = [set() for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, int(sqrt(i))+1):
        if i%j==0:
            factors[i].add(j)
            factors[i].add(i//j)
"""
class PrimeTable:

    #use MAXN = 10**6 (more if allowed)
    def __init__(self, n:int) -> None:
        self.n = n
 
        self.primes = []
        self.min_div = [0] * (n+1)
        self.min_div[1] = 1
 
        mu = [0] * (n+1)
        phi = [0] * (n+1)
        mu[1] = 1
        phi[1] = 1
 
        for i in range(2, n+1):
            if not self.min_div[i]:
                self.primes.append(i)
                self.min_div[i] = i
                mu[i] = -1
                phi[i] = i-1
            for p in self.primes:
                if i * p > n: break
                self.min_div[i*p] = p
                if i % p == 0:
                    phi[i*p] = phi[i] * p
                    break
                else:
                    mu[i*p] = -mu[i]
                    phi[i*p] = phi[i] * (p - 1)
 
    def is_prime(self, x:int):
        if x < 2: return False
        if x <= self.n: return self.min_div[x] == x
        for p in self.primes:
            if p * p > x: break
            if x % p == 0: return False
        for i in range(self.n+1, int(sqrt(x))+1):
            if x % i == 0: return False
        return True
    
    def prime_factorization(self, x:int):
        for p in self.primes:
            if p * p > x or x <= self.n: break
            if x % p == 0:
                cnt = 0
                while x % p == 0: 
                    cnt += 1
                    x //= p
                yield p, cnt
        for p in range(len(self.min_div), int(sqrt(x))+1):
            if x <= self.n: break
            if x % p == 0:
                cnt = 0
                while x % p == 0: cnt += 1; x //= p
                yield p, cnt
        while (1 < x and x <= self.n):
            p, cnt = self.min_div[x], 0
            while x % p == 0: cnt += 1; x //= p
            yield p, cnt
        if x >= self.n and x > 1:
            yield x, 1
    
    def get_factors(self, x:int):
        """ Not in ascending order"""
        factors = [1]
        for p, b in self.prime_factorization(x):
            n = len(factors)
            for j in range(1, b+1):
                for d in factors[:n]:
                    factors.append(d * (p ** j))
        return factors

#PT = PrimeTable(N)
#print(PT.get_factors(10))
def process(arr):
    l, r = arr   
    D = ddc(int)
    MAX = 0
    Cache = {}
    def dfs(x,s):
        if x>r: return []
        nonlocal MAX
        MAX = max(MAX, s)
        if (x,s) in Cache: return Cache[(x,s)]
        
        Cache[(x,s)] = sorted([s] + dfs(x*2, s+1) + dfs(x*3, s+1))
        return Cache[(x,s)]

    ans = 0
    for i in range(l, min(r+1, l+1000)):
        this = dfs(i, 1)
        ans += bisect_right(this, MAX) - bisect_right(this, MAX-1)
    
    return [MAX, ans]
   
    
    Cache = {}
    def dfs(x):
        if x in Cache: return Cache[x]
        if x>r: return [0, 1]
        m = 0
        s,val = dfs(x*2)
        D[s+1]+=val
        m = s

        s,val = dfs(x*3)
        D[s+1]+=val
        m = max(m, s)

        Cache[x] = [m, D[m]]
        return Cache[x]


    m = max(D.keys())
    return [m, D[m]]

        

        
        
def main():
    #T-testcases

    for _ in range(intin()):
        arr = mapin()
        #arr = input()
        ans = process(arr)
        print(*ans)
        #print("Case #{0}: {1}".format(_+1, ans))
    

#----------------------------------------------

if __name__ == "__main__":
    main()