class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ##Just by initial thoughts if there is a cycle in the graph It makes it impossible 

        ##Can use DFS to determine if there is a cycle
        ##It having a cycle doesnt always mean it wont work, if the cycle has a node that can be completed it will work
        ##Thats why i check if preMap[crs] == [] and if it is it means no pre req so it can be completed 
        ## which is why i also remove it from visiting set when im done with it 
        ##Lastly i have a for loop to go through each node as courses may not be connected graph fully 
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)


        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True 
            
            visiting.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            visiting.remove(crs)
            preMap[crs] = [] 
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True