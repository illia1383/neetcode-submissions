class Solution:
    def rob(self, nums: List[int]) -> int:
        #You cant rob house 0 and last index house 


        #We  might not be able to do this without a dp array 

        return max(nums[0], self.helper(nums[1:]),self.helper(nums[:-1]))
    
    def helper(self,nums):
        rob1,rob2 = 0,0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2 