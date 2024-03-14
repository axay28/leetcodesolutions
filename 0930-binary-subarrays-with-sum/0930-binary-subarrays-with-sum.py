class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = Counter({0: 1}) 
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            result += counter[prefix_sum - goal]
            counter[prefix_sum] += 1
        return result
