class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter=collections.Counter()
        for c in s:
            counter[c]+=1
        for i,v in enumerate(s):
            if counter[v]==1:
                return i
        return -1
        