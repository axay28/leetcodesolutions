class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        cache={}
        def helper(index,remwalls):
            if remwalls<=0:
                return 0
            if index==len(cost):
                return float("inf")
            if(index,remwalls) in cache:
                return cache[(index,remwalls)]
            painting=cost[index]+helper(index+1,remwalls-1-time[index])
            nopainting=helper(index+1,remwalls)
            cache[(index,remwalls)]=min(painting,nopainting)
            return cache[index,remwalls]
            
        return helper(0,len(cost))