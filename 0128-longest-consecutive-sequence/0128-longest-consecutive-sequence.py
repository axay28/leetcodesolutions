class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setn=set(nums)
        longest=0
        for num in nums:
            if(num-1) not in setn:
                length=1
                while(num+length) in setn:
                    length+=1
                longest=max(longest,length)
        return longest
        