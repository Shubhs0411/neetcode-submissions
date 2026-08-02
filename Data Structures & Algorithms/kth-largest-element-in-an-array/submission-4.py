class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]

        for num in nums:
            heapq.heappush(heap, num)
        
        for i in range(len(nums)-k,-1,-1):
            res=heapq.heappop(heap)
        return res

        