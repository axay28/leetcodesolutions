class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        index=0
        for num in nums:
            if num>nums[index]:
                index+=1
        return index
    
        