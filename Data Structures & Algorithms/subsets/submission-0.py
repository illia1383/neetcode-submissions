class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            #Base case, means that we are at the end of our tree and we want to add it 
            if i >= len(nums):
                res.append(subset.copy())
                return 
            #Add the current Num
            subset.append(nums[i])
            dfs(i+1)
            #Not add the current num
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res