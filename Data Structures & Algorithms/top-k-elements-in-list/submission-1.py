class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k is the top k most frequent elements 
        #Solution should be O(n) and o(n) space


        count = {}
        #ONE KEY NOTE IS TO ADD n + 1 buckets to not get out of bounds error freq 0 will remain unsued becuase no num has 0 freq 
        freq = [[] for i in range(len(nums) + 1)]


        for num in nums:
            count[num] = 1 + count.get(num,0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res 


        