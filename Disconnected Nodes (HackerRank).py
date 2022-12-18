from collections import defaultdict as ddc
def getMaxNewEdges(g_nodes, g_from, g_to,disconnected_nodes):
    graph = ddc(set)
    n = g_nodes
    for a,b in zip(g_from, g_to):
        graph[a-1].add(b-1)
        graph[b-1].add(a-1)
    
    visited = [False]*n
    
    def dfs(u):
        visited[u] = True
        ans = 1
        
        for v in graph[u]:
            if not visited[v]:
                ans += dfs(v)
        
        return ans
    
    
    poss = []
    for ele in disconnected_nodes:
        poss.append(dfs(ele-1))
    
    left = n - sum(poss)
    ans = max(ele*left for ele in poss)
    
    for i in range(n):
        if not visited[i]:
            ans -= (dfs(i) - 1)
    
    
    return ans
    


print(getMaxNewEdges(4, [1], [2], [1,3]))
print(getMaxNewEdges(6, [1,1,2,4], [2,3,3,5], [2,4]))
    
    