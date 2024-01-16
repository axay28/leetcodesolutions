class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap=[]
        for i,row in enumerate(mat):
            soldiers=sum(row)
            heapq.heappush(heap,(soldiers,i))
        
        return [heapq.heappop(heap)[1] for x in range(k)]