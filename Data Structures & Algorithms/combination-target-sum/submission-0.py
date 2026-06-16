class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            for j in range(i, len(nums)): #this inlcudes i 
                if total + nums[j] > target: #This is the part where it stops us from exploring useless paths
                    return 
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        dfs(0, [], 0)
        return res



