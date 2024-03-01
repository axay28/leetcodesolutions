class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        if rows==0:
            return False
        cols=len(matrix[0])
        l,r=0,rows*cols-1
        while l<=r:
            m=l+(r-l)//2
            candidate=matrix[m//cols][m %cols]
            if target==candidate:
                return True
            else:
                if target<candidate:
                    r=m-1
                else:
                    l=m+1
        return False
        