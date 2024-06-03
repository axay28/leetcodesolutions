class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j,s_,t_=0,0,set(),set()
        lens,lent=len(s),len(t)
        while i < lens and j < lent:
            if s[i] == t[j]:
                j += 1
            i += 1
        if j == lent:
            return 0
        return lent - j