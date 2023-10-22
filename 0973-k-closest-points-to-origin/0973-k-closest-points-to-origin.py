class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        ans=[]
        for x,y in points:
            distance=x**2+y**2
            minheap.append([distance,x,y])
        heapq.heapify(minheap)
        
        while k>0 and minheap:
            distance,x,y=heapq.heappop(minheap)
            ans.append([x,y])
            k-=1
        return ans