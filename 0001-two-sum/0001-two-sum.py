class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousmap={}
        for index,number in enumerate(nums):
            diff= target - number
            if diff in previousmap:
                return [previousmap[diff],index]
            previousmap[number]=index
        return
        
        