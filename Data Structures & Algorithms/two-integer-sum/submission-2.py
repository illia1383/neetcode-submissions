class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}

        for i,nums in enumerate(nums):
            diff = target - nums
            if diff in seen:
                return [seen[diff], i ]
            seen[nums] = i 