class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort() 
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        unique_sides = len(set(nums))

        if unique_sides==1:
            return "equilateral"
        if unique_sides==2:
            return "isosceles"
        if unique_sides==3:
            return "scalene"
        
        