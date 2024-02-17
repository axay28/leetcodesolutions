class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        for i in range(n - 2, -1, -1):
            nums[i] = max(nums[i] + (nums[i+2] if i + 2 < n else 0), nums[i+1])
        return nums[0]
