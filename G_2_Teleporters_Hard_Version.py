"""THIS TEMPLATE belongs to anuj_negi"""

#Try to use bisect in case of binary search, bisect_left, bisect_right
#Try to use sortedcontainers when available
#Try to use Multiset when available
from bisect import *

#into = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
#def input(): return into().decode().strip()

def intin(): return int(input())
def mapin(): return list(map(int, input().split()))
def strin(): return input().split()   

#----------------------------------------------

INF = 1<<64     #Or use 10**20
mod = 10**9 + 7
yes = "YES"
no = "NO"
even = "EVEN"
odd = "ODD"
alice = "ALICE"
bob = "BOB"

#----------------------------------------------
#Starts from here

def process(arr, n, c):
    def pr(arr, n, c):    
        
        new = [(min(i, n-i+1)+ ele, i, ele) for i, ele in enumerate(arr, start=1)]
        pref = [0]*n + [1e9]
        ans = 0
        curr = 0
        new.sort()
        tot = set()
        j = 0
        for cc, i, e in new:
            curr += cc
            pref[j] = curr
            if pref[j]<=c:
                ans = j+1
                tot.add(i)
            j+=1
        
        ans = 0
        for cc, i, e in new:
            curr = e+i
            c-=curr
            temp = 0
            if i not in tot:
                temp = -1

            if c>=0:
                j = bisect_right(pref, c+cc)
                ans = max(ans, j+temp)
            c+=curr
        
        return ans
  
    
    def pr2(arr, n, c):
        new = [i+ele for i, ele in enumerate(arr, start=1)]
        new.sort()
        ans = 0
        for ele in new:
            if c>=ele:
                c-=ele  
                ans+=1
            else: break
 
        return ans

    return max(pr(arr, n, c), pr2(arr, n, c))
        
def main():
    #T-testcases
    for _ in range(int(input())):
        n, c = mapin()
        #graph = graphin(n)
        arr = mapin()
        ans = process(arr, n, c)
        print(ans)
        #print("Case #{0}: {1}".format(_+1, ans))
    




if __name__ == "__main__":
    main()