import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Using a max heap is the way to go
        # to convert a min heap to a max heap is to convert all the nums to - to invert it and it becomes a max 

        stones = [-s for s in stones]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second =  heapq.heappop(stones)
            if second > first: 
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0]) ## This is to invert it back 