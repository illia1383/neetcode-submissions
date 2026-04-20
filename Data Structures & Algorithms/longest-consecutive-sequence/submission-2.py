class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        consec = 0 
        for i in numSet:
            length = 1
            if((i-1)not in numSet):

                while (i+length) in numSet:
                    length +=1
            consec = max(consec,length)
        return consec

            