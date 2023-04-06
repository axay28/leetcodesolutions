class Solution(object):
    def twoSum(self, nums, target):
        seen = {} # 2 7 11 15 9
        for i, num in enumerate(nums): ## i=0 num=2
            if target - num in seen:
                return [seen[target - num], i] 
            seen[num] = i # 0,2 0,1 
        return [-1, -1]