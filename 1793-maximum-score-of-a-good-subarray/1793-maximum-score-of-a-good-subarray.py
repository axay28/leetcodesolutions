class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l=r=k
        res=nums[k]
        current=nums[k]
        while l>0 or r<len(nums)-1:
            left=nums[l-1] if l>0 else 0
            right=nums[r+1] if r<len(nums)-1 else 0
            if left>right:
                l-=1
                current=min(current,left)
            else:
                r+=1
                current=min(current,right)
                
            res=max(res,current*(r-l+1))
        return res