class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=collections.Counter()
        for c in s:
            count[c]+=1
        for i,x in enumerate(s):
            if count[x]==1:
                return i
        return -1
        