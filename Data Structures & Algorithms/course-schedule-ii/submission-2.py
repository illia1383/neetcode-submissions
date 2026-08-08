class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)] #Coure -> prerequisites
        indegree = [0] * numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        

        q = deque()
        res = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        print(q)
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(res) != numCourses:
            return []

        return res



        
        