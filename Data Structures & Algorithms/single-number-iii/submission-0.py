class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        odd_set = set()

        for i in nums:
            if i not in odd_set:
                odd_set.add(i)
            else:
                odd_set.remove(i)
        
        return list(odd_set)