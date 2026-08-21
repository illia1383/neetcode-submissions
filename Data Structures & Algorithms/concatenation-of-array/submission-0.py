class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = nums + nums.copy()
        return res 