class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #You have to determine if there is a cylce, because if there is then you wont be able to complete the courses 

        #Using Topoligical sort 

        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        print(adj)
        for course, preq in prerequisites:
            indegree[preq] += 1
            adj[course].append(preq)
        print(adj)
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        finish = 0
        while q:
            node = q.popleft()

            finish += 1

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses

