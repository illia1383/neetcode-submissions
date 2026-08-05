class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score = [0] * (n + 1)

        for u,v in trust:
            score[u] -= 1
            score[v] += 1

        for i in range(len(score)):
            print(i)
            if i == 0:
                continue
            if score[i] == n - 1:
                return i
        return -1