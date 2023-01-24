"""THIS TEMPLATE belongs to anuj_negi"""

#Try to use bisect in case of binary search, bisect_left, bisect_right
#Try to use sortedcontainers when available
#Try to use Multiset when available
from bisect import *
from heapq import *
#from functools import cache, lru_cache
from math import *
from collections import defaultdict as ddc
from collections import Counter
from functools import *
from itertools import *
from sys import setrecursionlimit
import io,os

into = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return into().decode().strip()

def intin(): return int(input())
def mapin(): return list(map(int, input().split()))
def strin(): return input().split()   
def graphin(m):
    zz = ddc(set)
    for i in range(m):
        a, b = mapin()
        zz[a].add(b)
        zz[b].add(a)
    
    return zz

#----------------------------------------------

INF = 1<<64     #Or use 10**20
mod = 10**9 + 7
yes = "YES"
no = ":("
even = "EVEN"
odd = "ODD"
alice = "ALICE"
bob = "BOB"

#----------------------------------------------
#Starts from here

def process(arr):
    n = len(arr)

    a, b, c = list(arr[0]), list(arr[1:-1]), list(arr[-1])
    
    if arr[1]=='b':
        a, c = arr[0], arr[-1]
        b = arr[1:-1]
        if a>=b and c>=b: return [a,b,c]
        if a<=b and c<=b: return [a,b,c]
    
        return [no]
    
    else:
        a,b = arr[0], arr[1]
        c = arr[2:]
        if a>=b and c>=b: return [a,b,c]
        if a<=b and c<=b: return [a,b,c]
    
        return [no]
        
def main():
    #T-testcases
    for _ in range(int(input())):
        arr = input()
        ans = process(arr)
        print(*ans)
        #print("Case #{0}: {1}".format(_+1, ans))
    


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
"""
-> THIS IS A Interval Based Segmented Trees
-> Can be modified or used later for similar
"""

class IntervalSeg:
    def __init__(self):
        self.Seg = ddc(int)
        self.otherAdded = ddc(int)
        
    def update(self, s, e, l = 0, r = 10**9, index = 1):
        if r<=s or e<=l: return
        if s<=l<r<=e:
            self.Seg[index]+=1
            self.otherAdded[index]+=1
            
        else:
            m = (l+r)//2
            self.update(s, e, l, m, 2*index)
            self.update(s, e, m, r, 2*index + 1)
            self.Seg[index] = self.otherAdded[index] + max(self.Seg[2*index], self.Seg[2*index + 1])
    
    def use(self, start, end):
        self.update(start, end)
        return self.Seg[1]

#----------------------------------------------
#FOR nCr
class nCr:
    def __init__(self):
            
        self.fact = [1]*(1000001)
        self.factinv = [1]*(1000001)
        for i in range(1, 1000001):
            self.fact[i] = self.fact[i-1] * i % mod
            
        self.factinv[-1] = exponentiation(self.fact[-1], mod-2, mod)
        for i in range(1000000-1, 1, -1):
            self.factinv[i] = self.factinv[i+1] * (i+1) % mod

    def C(self, n, r):
        if n<r or r<0: return 0
        return self.fact[n] * self.factinv[r] % mod * self.factinv[n-r] % mod

#----------------------------------------------
#This is a better way to find the primes/prime factors/factors faster
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


#----------------------------------------------
#Use this when really needed 
# Such as - Getting TLE because some TC can cause O(n^2) on pre-built HASHMAPS
def custom_hash(x):
    return x // 1000000007, x % 1000000007

#----------------------------------------------
#Subarray size - Rolling Hash - Custom
def hash_it(arr, size, mod = (10**9 + 7)):
    """
    mul -> must be greater than max(arr)
    rest can be modified
    """
    if not size: return 
    mul, hashh, div = 256, 0, (1<<(8*size-8))%mod
    
    C = ddc(list)
    for i in range(size):
        hashh = (mul * hashh + arr[i])%mod
    
    C[hashh].append(0)
    
    for i in range(len(arr)-size):
        #update the hashh
        hashh = (mul*(hashh-arr[i]*div) + arr[i+size])%mod
        C[hashh].append(i+1)
    
    return C

#----------------------------------------------

def LIS(arr, n):
    dp = [10**9]*(n+1)
        
    for ele in arr:
        dp[bisect_left(dp, ele)] = ele
    #print(dp)
    return bisect_left(dp, 10**9)

#----------------------------------------------
#Fast base^exp 
def exponentiation(bas, exp, mod = 10**9 + 7):
    t = 1
    while(exp > 0): 
  
        if (exp % 2 != 0):
            t = (t * bas) % mod
  
        bas = (bas * bas) % mod 
        exp //= 2
    return t % mod

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

#----------------------------------------------


if __name__ == "__main__":
    main()