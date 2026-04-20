import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Min heap and keep popping until k is 0 so we get smallest elements 
        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist,x,y])

        #Min heap reads lexigraphically so thats why it able to sort by the first num
        heapq.heapify(minHeap)
        print(minHeap)
        res = []
        while k > 0:
            dist,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k -=1 
        return res 


