class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if len(nums)==1:
            return [nums[0]]
        freq=collections.Counter(nums)
        h=[(-freq,n) for n,freq in freq.items() ]
        heapq.heapify(h)
        ans=heapq.nlargest(k,freq.keys(),key=freq.get)
        return ans
        