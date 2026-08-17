class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        text= s.rstrip()
        res = text.split(" ")
        print(res)
        return len(res[-1])