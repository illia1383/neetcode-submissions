class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] *  numCourses

        adj = [[] for i in range(numCourses)]

        for crs, pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        finish = 0
        output = []
        
        while q:
            node = q.popleft()
            output.append(node)
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if finish != numCourses:
            return []
        return output[::-1]
        
