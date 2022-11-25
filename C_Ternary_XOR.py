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

def intin(): return int(input())
def mapin(): return map(int, input().split())
def strin(): return input().split()

#----------------------------------------------

"""
SOME FACTS THAT CAN BE USED LATER - 

-> if n is prime, then -> (a**(n-1)) % n = 1

-> When cases like DEFICIENT CITY to SURPLUS CITY, work on BFS using SURPLUS city and check for DEFICIENT city

-> PALINDROMEs and str-len FACTORS have some relations. if P = XQ where P, X, Q are palindromes, then X have the possible length in Factors of 'n'

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

INF = 10**20
mod = 1000000007

#----------------------------------------------

def hashit(arr, size, mod = (10**9 + 7)):
    #Subarray size - Rolling Hash - Custom
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

def exponentiation(bas, exp, mod = (10**9 + 7)):
    t = 1
    while(exp > 0): 
  
        if (exp % 2 != 0):
            t = (t * bas) % mod
  
        bas = (bas * bas) % mod 
        exp //= 2
    return t % mod

#----------------------------------------------

def MOD(p, q=1, mod = 1000000007):
    expo = 0
    expo = mod - 2
 
    while (expo):
        if (expo & 1):
            p = (p * q) % mod
        q = (q * q) % mod
        expo >>= 1
    return p

#----------------------------------------------

yes = "YES"
no = "NO"
even = "EVEN"
odd = "ODD"
alice = "ALICE"
bob = "BOB"

#------------------------

def graphin(n):
    zz = ddc(set)
    for i in range(n-1):
        a, b = mapin()
        zz[a].add(b)
        zz[b].add(a)
    
    return zz

        
def process(arr, n):
    All = [[0,0], [0,1],[0,2]]
    All2 = [[0,0], [1,0],[1,1]]
    a, b = 1,1
    flag = 0
    for ele in map(int, arr[1:]):
        if not flag:
            a = a*10 + All2[ele][0]
            b = b*10 + All2[ele][1]
        else:   
            a = a*10 + All[ele][0]
            b = b*10 + All[ele][1]
        if ele==1:
            flag = 1
        
 
    print(a)
    print(b)
        
def main():
    #T-testcases
    for _ in range(int(input())):
        n = intin()
        #graph = graphin(n)
        arr = input()
        ans = process(arr, n)
        #print("Case {0}: {1}".format(ans, _+1))
    
#--------------------------
if __name__ == "__main__":
    main()