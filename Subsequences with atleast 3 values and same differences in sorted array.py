class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        C = Counter(nums)
        
        #print(sorted(nums))
        @cache
        def dfs(this, k):
            if this in C:
                m = C[this]
                return m + (m*dfs(this+k, k))
            return 0
        
        ans = 0
        
        for key1 in C:
            for key2 in C:
                nex = 2*key2 - key1
                if key2>key1 and nex in C:
                    #print(key1, key2, nex)
                    #print(C[key1]*C[key2]*dfs(nex, key2-key1))
                    ans += C[key1]*C[key2]*dfs(nex, key2-key1)
                    #print()
        
        #print(list(range(1, 101)))
        for key in C:
            if C[key]>2:
                m = C[key]
                m = m*(m+1)//2
                ans += (1<<C[key]) - m - 1
                
        return ans