class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #So the difference between this and the  subsets 1 is that we add based on index of the integer not just what it is 


        res = []
        nums.sort()


        def dfs(i, subsets):
            if i == len(nums):
                res.append(subsets.copy())
                return 
            
            subsets.append(nums[i])
            dfs(i+1, subsets)
            subsets.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, subsets)

        dfs(0, [])
        return res 
        
            
