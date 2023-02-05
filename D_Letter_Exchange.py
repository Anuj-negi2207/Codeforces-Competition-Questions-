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
uni = ['w', 'i', 'n']

def process(todo, checker, n):
    ans = []

    for a in uni:
        for b in uni:
            #print(a,b,checker[a][b])
            while checker[a][b]:
                j = checker[a][b].pop()
                if checker[b][a]:
                    k = checker[b][a].pop()
                    ans.append([j+1, a, k+1, b])
                else:
                    for c in uni:
                        if checker[b][c]:
                            k = checker[b][c].pop()
                            ans.append([j+1, a, k+1, b])
                            checker[a][c].append(k)
                            break
    
    for a in uni:
        for b in uni:
            #print(a,b,checker[a][b])
            while checker[a][b]:
                j = checker[a][b].pop()
                if checker[b][a]:
                    k = checker[b][a].pop()
                    ans.append([j+1, a, k+1, b])
                else:
                    for c in uni:
                        if checker[b][c]:
                            k = checker[b][c].pop()
                            ans.append([j+1, a, k+1, b])
                            checker[a][c].append(k)
                            break


    
    print(len(ans))
    for row in ans:
        print(*row)


            
         
        
        
def main():
    #T-testcases

    for _ in range(intin()):
        n = intin()
        todo = []
        checker = {}
        for a in uni:
            checker[a] = {}
            for b in uni:
                checker[a][b] = []
        
        for i in range(n):
            arr = input()
            todo.append(arr)
            if all(x in arr for x in uni):
                continue
            
            for test in [['w', 'i', 'n'], ['w', 'n', 'i'], ['n', 'i', 'w']]:
                a,b,c = test
                if all(x in arr for x in test[:-1]):
                    if arr.count(a)==2:
                        checker[a][c].append(i)
                    else:
                        checker[b][c].append(i)
                    break
            
            for x in uni:
                if arr.count(x)==3:
                    for y in uni:
                        if y!=x:
                            checker[x][y].append(i)
                    break
        
            

        process(todo, checker, n)
        #print("Case #{0}: {1}".format(_+1, ans))
    

#----------------------------------------------

if __name__ == "__main__":
    main()