class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr):
            if len(arr)<=1:
                return arr
            mid=len(arr)//2
            left=mergesort(arr[:mid])
            right=mergesort(arr[mid:])
            return merge(left,right)
        
        def merge(a,b):
            i,j=0,0
            result=[]
            while(i<len(a) and j<len(b)):
                if b[j]>a[i]:
                    result.append(a[i])
                    i+=1
                else:
                    result.append(b[j])
                    j+=1
            while(i<len(a)):
                result.append(a[i])
                i+=1
            while(j<len(b)):
                result.append(b[j])
                j+=1
            return result
        return mergesort(nums)