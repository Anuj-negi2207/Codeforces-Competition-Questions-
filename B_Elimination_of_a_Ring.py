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

INF = 1<<64     #Or use 10**20
mod = 1000000007

#----------------------------------------------
#Use this when really needed 
# Such as - Getting TLE because some TC can cause O(n^2) on pre-built HASHMAPS
def custom_hash(x):
    return x // 1000000007, x % 1000000007

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
#Fast base^exp 
def exponentiation(bas, exp, mod = (10**9 + 7)):
    t = 1
    while(exp > 0): 
  
        if (exp % 2 != 0):
            t = (t * bas) % mod
  
        bas = (bas * bas) % mod 
        exp //= 2
    return t % mod

#----------------------------------------------
#Fast multiplication
def fastMul(a, b, mod = (10**9 + 7)):
    t = 0
    while(b > 0):   

        if (b % 2 != 0):
            t = (t + a) % mod

        a = (a + a) % mod 
        b //= 2
    return t % mod

#----------------------------------------------

#Returns P*Q^-1 % Mod
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

def SortArrayMinSwap(arr, n):
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

#------------------------

def graphin(n):
    zz = ddc(set)
    for i in range(n-1):
        a, b = mapin()
        zz[a].add(b)
        zz[b].add(a)
    
    return zz


def process(arr, n):
    if n==1: return 1
    C = Counter(arr)
    #I know that if there are exactly 2 distinct value, n = even and 1 2 1 2 
    #but more distinct, 1 2 3 1 2 = 3, 1 2 3 4 1 2 = 4
    if not n%2 and len(C.keys())==2: return 1 + (n//2)
    stack = []  
    ans = 0
    for ele in arr:
        while len(stack)>1 and stack[-2]!=ele:
            stack.pop()
            ans+=1
        stack.append(ele)

    while len(stack)>1 and ((stack[-2]==stack[-1]) or (stack[-1]==stack[0])):
        stack.pop()
    
    while stack:    
        stack.pop()
        ans+=1
        while len(stack)>1 and stack[-1]==stack[0]:
            stack.pop()
    
    return max(n, ans)


    print(stack)

    return ans
    val = list(C.keys())
    #print(val)
    val.sort(key = lambda x: -C[x])
    val = val[0]

    ans = 0
    for ele in arr:
        if ele==val:
            ans += 1
            continue
        stack.append(ele)
        while len(stack)>1 and ((stack[-2]==stack[-1])):
            stack.pop()
    
    while len(stack)>1 and ((stack[-2]==stack[-1]) or (stack[-1]==stack[0])):
        stack.pop()
    
    #   print(stack)
    return ans + process(stack, len(stack))
        
def main():
    #T-testcases
    for _ in range(int(input())):
        n = intin()
        #graph = graphin(n)
        arr = list(mapin())
        ans = process(arr, n)
        print(ans)
        #print("Case #{0}: {1}".format(_+1, ans))
    
#--------------------------
if __name__ == "__main__":
    main()