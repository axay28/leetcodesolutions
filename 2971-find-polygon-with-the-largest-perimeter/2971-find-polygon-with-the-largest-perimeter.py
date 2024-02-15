class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        while nums:
            if max(nums) < sum(nums)-max(nums):
                return sum(nums)
            else:
                nums.remove(max(nums))
        return -1
        