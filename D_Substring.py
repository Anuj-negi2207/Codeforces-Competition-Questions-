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
def mapin(): return map(int, input().split())
def strin(): return input().split()   
def graphin(m):
    zz = ddc(set)
    for i in range(m):
        a, b = mapin()
        zz[a].add(b)
        
    return zz

#----------------------------------------------

INF = 1<<64     #Or use 10**20
mod = 10**9 + 7

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

yes = "YES"
no = "NO"
even = "EVEN"
odd = "ODD"
alice = "ALICE"
bob = "BOB"

#----------------------------------------------

def process(arr, graph, n):
    indeg = ddc(int)
    dp = [[0]*26 for i in range(n)]
    vis = [False]*n
    chain = [False]*n
    for a in graph:
        for b in  graph[a]:
            indeg[b]+=1
    
    ans = [-1]
    
    def dfs(uu):
        stack = [uu]
        stack2 = [uu]
        vis[uu-1] = True
        
        while stack:
            u = stack.pop()
            vis[u-1] = True
            chain[u-1] = True
            for v in graph[u]:
                if not vis[v-1]: 
                    stack.append(v)
                    stack2.append(v)
        
        print(stack2)

        while stack2:
            u = stack2.pop()
            for v in graph[u]:  
                if chain[v-1]:
                    #print(u, v)
                    #print("yes")
                    ans[0] = 1e9
                    return
                for i in range(26):
                    dp[u-1][i] = max(dp[u-1][i], dp[v-1][i])
            
            dp[u-1][ord(arr[u-1])-97]+=1
            ans[0] = max(ans[0], dp[u-1][ord(arr[u-1])-97])
            chain[u-1] = False
        

    #print(graph)   
    
    Q = []
    for i in range(n):
        if indeg[i+1]==0:
            Q.append(i+1)
            vis[i]= True
    
    while Q:
        #print(Q)
        u = Q.pop(0)
        dp[u-1][ord(arr[u-1])-97]+=1
        ans[0] = max(ans[0], dp[u-1][ord(arr[u-1])-97])
            

        chain[u-1] = True
        for v in graph[u]:
            if chain[v-1]:
                ans[0] = 1e9
                break
            if not vis[v-1]:
                vis[v-1] = True
                Q.append(v)
                for i in range(26):
                    dp[v-1][i] = max(dp[u-1][i], dp[v-1][i])


    if ans[0]==1e9: return -1
    return ans[0]
        
        
def main():
    #T-testcases
    n, m = mapin()
    arr = input()
    graph = ddc(set)
    for i in range(m):
        a, b = mapin()
        graph[a].add(b)

    ans = process(arr, graph, n)
    print(ans)
    #print("Case #{0}: {1}".format(_+1, ans))
    
#--------------------------
if __name__ == "__main__":
    main()