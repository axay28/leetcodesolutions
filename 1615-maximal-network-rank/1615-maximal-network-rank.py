class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(set)
        maxr=0
        for road in roads:
            adj[road[0]].add(road[1])
            adj[road[1]].add(road[0])
        for i in range(n):
            for j in range(i+1,n):
                current=len(adj[i])+len(adj[j])
                if j in adj[i]:
                    current-=1
                maxr=max(maxr,current)
        return maxr
            
        