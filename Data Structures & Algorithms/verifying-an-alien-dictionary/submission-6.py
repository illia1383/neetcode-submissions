class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        adj = {c: i for i,c in enumerate(order)}
        

        for word in range(len(words) - 1):
            w1, w2 = words[word], words[word + 1]
            
            for j in range(len(w1)):
                if j == len(w2):
                    return False 
                if w1[j] != w2[j]:
                    if adj[w1[j]] > adj[w2[j]]:
                        return False
                    break 
        return True  
                        

