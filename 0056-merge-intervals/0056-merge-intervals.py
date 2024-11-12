class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged=[]
        i=0
        while i <len(intervals):
            start,end=intervals[i][0],intervals[i][1]
            j=i+1
            while j<len(intervals) and (intervals[j][0]<=end or intervals[j][1]<=end):
                end=max(end,intervals[j][1])
                j+=1
            merged.append([start,end])
            i=j
        return merged
        