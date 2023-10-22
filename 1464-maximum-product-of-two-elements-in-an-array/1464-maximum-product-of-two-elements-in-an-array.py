class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_heap=[]
        for num in nums:
            heapq.heappush(max_heap, num)
            if len(max_heap) > 2:
                heapq.heappop(max_heap)

        
        largest1, largest2 = heapq.heappop(max_heap), heapq.heappop(max_heap)
        return (largest1-1)*(largest2-1)
