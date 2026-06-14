class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = (heapq.heappop(maxHeap))
            y = (heapq.heappop(maxHeap))

            new = y - x

            if new > 0: 
                heapq.heappush(maxHeap, - new)
            print(maxHeap)
        print(maxHeap)
        return (-1 * maxHeap[0]) if maxHeap else 0
