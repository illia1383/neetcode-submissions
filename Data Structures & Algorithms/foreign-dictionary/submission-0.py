class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #if the second word is a prefix of the first word 
            #return ""
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1,w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        

        visited = {} #False #True: if in current path
        res = []
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True #Cycle detected 
                
            visited[c] = False #no longer in the path
            res.append(c)

        for i in adj:
            if dfs(i):
                return "" #Cycle detected breaks rules 
        res.reverse()
        return "".join(res)

