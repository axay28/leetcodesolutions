class Solution:
    def pivotInteger(self, n: int) -> int:
        l,r=1,n
        first=l
        second=n
        if n==1:
            return n
        while l<r:
            if first<second:
                first+=l+1
                l+=1
            else:
                second+=r-1
                r-=1
            if first==second and l+1==r-1:
                return r-1
        return -1