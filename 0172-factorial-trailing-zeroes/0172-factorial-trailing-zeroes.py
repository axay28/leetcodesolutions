class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact=1
        for i in range(2,n+1):
            fact*=i
        count=0
        while fact%10==0:
            count+=1
            fact//=10
        return count