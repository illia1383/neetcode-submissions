class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #The outer loop needs to parse through the input array 
        #The inner loop needs to create our substrings 
        #The condition of the inner loop is that it needs to make palindromes



        res = []
        part = []
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return 
            for j in range(i, len(s)):
                if self.isPali(s, i,j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    


            