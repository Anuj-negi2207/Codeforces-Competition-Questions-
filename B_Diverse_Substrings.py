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

-> When all substrings are said to be checked, we can go for 2 loops (With 100 limit of inner loop, minimize the memory)
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

def check(arr, n, win):
    if win>n: return 0
    All = set()
    ans = 0

    C = ddc(int)
    for i in range(win):
        C[arr[i]]+=1
        All.add(arr[i])
    if all(C[str(k)]<=len(All) for k in range(10)):
        ans += 1
    
    for i in range(n-win):
        C[arr[i]]-=1
        C[arr[i+win]]+=1
        if all(C[str(k)]<=len(All) for k in range(10)):
            ans += 1

    return

def process2(arr, n):
    ans = 0
    curr = len(set(arr))

    for i in range(n):
        C = [0]*10
        All = 0
        for j in range(i, min(i+228, n)):
            ele = ord(arr[j]) - ord('0')
            if C[ele]==0: All+=1
            C[ele]+=1
            if max(C)<=All:
                ans += 1
        
        #print(i, ans)
    
    return ans



def process(arr, n):
    
    ans = n*(n+1)//2
    
    last = arr[0]
    i = 0

    while i<n:
        curr = 0
        j = i
        while i<n and arr[i]==last:
            curr+=1
            i+=1

        ans -= curr*(curr-1)//2
        if curr>2:
            if j+2>=curr: ans += curr-2
            if (j+(2*curr)-3)<n: ans += curr-2
        if i<n:
            last = arr[i]
    
    return ans
    ans = 0


    C = ddc(int)
    All = set()
    
    curr = 0
    k = 0
    i = 0
    while i<n:
        while i<n and all(C[j]<=len(All) for j in range(10)):    
            ans += curr
            ele = int(arr[i])
            if ele not in All:
                All.add(ele)
            C[ele]+=1   
            curr+=1
            i+=1
        

        while any(C[j]>len(All) for j in range(10)):
            C[int(arr[k])]-=1
            if C[int(arr[k])]==0:
                All.remove(int(arr[k]))
            k+=1
            n-=1
            curr-=1
    
    ans += curr
        #print(curr, k)
        #ans += curr*(curr+1)//2
        
        #print(C, j, k)
        
    return ans
            

        
        
def main():
    #T-testcases
    for _ in range(int(input())):
        n = intin()
        #graph = graphin(n)
        arr = input()
        ans = process2(arr, n)
        print(ans)
        #print("Case #{0}: {1}".format(_+1, ans))
    
#--------------------------
if __name__ == "__main__":
    main()