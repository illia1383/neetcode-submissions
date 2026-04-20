import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # To maintain the kth largest element in a stream 
        # of numbers we do not need to store all values 
        # we only need to keep track of the k largest elements seen so far 

        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)


    # The smallest k element will allways be at the root
    # This is because we are ensuring that the heap is < k elements 
    # so auto the kth element will be at the top 
    # and pop the 
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
