class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        count=0
        for i in range(0,n-2):
            left,right=i+1,n-1
            while left<right:
                if target>nums[left]+nums[i]+nums[right]:
                    count+=right-left
                    left+=1
                else:
                    right-=1
        return count