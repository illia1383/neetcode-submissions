class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:    
        ##Easiest solution is to create a set of this as well and if the set is a different size it means the original has a dup

        newList = set(nums)
        if len(newList) < len(nums):
            return True 
        return False