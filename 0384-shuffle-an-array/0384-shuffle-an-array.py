class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.mylist=list(nums)
        

    def reset(self) -> List[int]:
        return self.mylist
        

    def shuffle(self) -> List[int]:
        ans=self.nums
        for i in range(len(ans)):
            j=random.randrange(i,len(ans))
            ans[j],ans[i]=ans[i],ans[j]
        return ans
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()