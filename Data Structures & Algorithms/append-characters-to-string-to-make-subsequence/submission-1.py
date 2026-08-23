class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # two pointers, one at the start of S and one at the start of T 
        # whatever s has that are in t we subtract their length and add the rest to the end of S 



        res = len(t) # initially we assume we have to add the full thing

        l,r = 0,0 

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                res -= 1 
                r += 1
            l += 1 
        return res 