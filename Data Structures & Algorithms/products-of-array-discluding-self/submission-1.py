class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Pre fix, suffix needed 
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n 

        ## 3 cases 
            ## position 0 of the array there will be no prefix
            ## Last position of the array there will be no suffix 
            ## middle position will need to get both the pre and suff 

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res