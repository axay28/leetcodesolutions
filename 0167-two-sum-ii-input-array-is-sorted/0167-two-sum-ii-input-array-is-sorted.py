class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        while l<=r:
            s=nums[l]+nums[r]
            if target==s:
                return l+1,r+1
            elif target>s:
                l+=1
            else:
                r-=1
                
                
        