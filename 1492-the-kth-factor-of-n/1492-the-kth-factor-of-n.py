class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        Factor=0
        i=1
        while i<=n:
            if n%i==0:
                Factor+=1
            if Factor==k:
                return i
            i+=1
        return -1
        