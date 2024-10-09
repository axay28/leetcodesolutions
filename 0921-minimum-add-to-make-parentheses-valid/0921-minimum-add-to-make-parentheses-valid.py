class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        adds=0
        openb=0
        for c in s:
            if c=="(":
                openb+=1
            else:
                if openb>0:
                    openb-=1
                else:
                    adds+=1
        return adds+openb