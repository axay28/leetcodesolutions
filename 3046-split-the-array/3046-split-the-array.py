class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        number=Counter(nums)
        a,b={},{}
        for k,v in number.items():
            if v>2:
                return False
            elif v==1:
                a[k]=1
            elif v==2:
                a[k]=1
                b[k]=1
        return True