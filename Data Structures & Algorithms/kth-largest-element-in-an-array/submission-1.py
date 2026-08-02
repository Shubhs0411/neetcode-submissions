import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        min_Heap=[]
        heapq.heapify(min_Heap)
        for num in nums:
            heapq.heappush(min_Heap, num)

            if len(min_Heap)>k:
                heapq.heappop(min_Heap)
        return min_Heap[0]

