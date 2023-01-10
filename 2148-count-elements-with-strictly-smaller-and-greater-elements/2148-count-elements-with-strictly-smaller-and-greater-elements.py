class Solution:
    def countElements(self, nums: List[int]) -> int:
        r=0
        d=min(nums)
        e=max(nums)
        for x in nums:
            if d<x<e:
                r+=1
        return r
        