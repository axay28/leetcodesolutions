class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        formula_sum=len(nums)*(len(nums)+1)//2
        real_sum=sum(nums)
        return formula_sum-real_sum