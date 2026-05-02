class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1 

        res = []

        # 1 indexed

        while l < r: 
            cur = numbers[l] + numbers[r]

            if cur > target: 
                r -= 1
            elif cur < target:
                l += 1
            else:
                res = [l + 1, r + 1]
                break 
        return res 
