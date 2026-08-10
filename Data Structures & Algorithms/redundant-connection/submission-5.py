class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        indegree = [0] * (len(edges) + 1)

        adj = [[] for _ in range(len(edges) + 1)]
        

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        
        q = deque()
        for i in range(len(indegree)):
            if i == 0:
                continue
            
            if indegree[i] == 1:
                q.append(i)
        print(q)
        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        res = []
        print(indegree)
        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        return []

