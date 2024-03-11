class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res=[]
        count=collections.Counter(s)
        for c in order:
            if c in count:
                res.append(c*count[c])
                del count[c]
        for c,no in count.items():
            res.append(c*no)
        return ''.join(res)
       
