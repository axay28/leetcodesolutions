class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def back(start,curr):
            
            res.append(curr[:])
            
            for i in range(start,n):
                
                curr.append(nums[i])
                back(i+1,curr)
                curr.pop()
        
        res=[]
        n=len(nums)
        
        back(0,[])
        
        return res
            
            
        