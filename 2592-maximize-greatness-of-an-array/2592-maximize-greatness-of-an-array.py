class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        xcount=0
        for num in nums:
            if num>nums[xcount]:
                xcount+=1
        return xcount
    
        