class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for c in range(n - m + 1):
            r = 0
            while r < m and haystack[c + r] == needle[r]:
                r += 1
            if r == m:
                return c
        return -1