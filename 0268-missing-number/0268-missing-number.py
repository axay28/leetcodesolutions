class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=set(nums)
        n=len(nums)+1
        for i in range(n):
            if i not in x:
                return i