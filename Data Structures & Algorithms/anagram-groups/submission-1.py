class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #We need to keep some sort of buckets essentially that hold each group 
        # the freq array we create will become the key, so if act and cat are anagrams they will have the same freq array count 
        # and by calling that key we add that to the same sub array in the res 
        res = defaultdict(list)

        for s in strs: 
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            print(f"this is count: {s}", tuple(count)) 
            res[tuple(count)].append(s)
        return list(res.values())


