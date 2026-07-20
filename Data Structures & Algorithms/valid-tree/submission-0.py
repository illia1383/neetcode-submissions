class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #A valid tree has no cycles and fully connected 

        visited = set()
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node, prev):
            if node in visited:
                return False 
            
            visited.add(node)
            for j in adj[node]:
                if j == prev:
                    continue
                if not dfs(j,node):
                    return False 
            return True

        return dfs(0,-1) and n == len(visited)
             


            