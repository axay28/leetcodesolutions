class Solution:
    def minimumLength(self, s: str) -> int:
        l,r=0,len(s)-1
        while l<r:
            if s[l] != s[r]:
                break 
            current=s[l]
            while l<=r and current==s[l]:
                l+=1
            while r>=l and current==s[r]:
                r-=1
        return max(r-l+1,0)
            