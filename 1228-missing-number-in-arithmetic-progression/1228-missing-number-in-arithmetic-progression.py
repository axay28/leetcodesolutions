class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        missing=(arr[-1]-arr[0])//len(arr)
        for x in range(1,len(arr)):
            if missing + arr[x-1]!=arr[x]:
                return missing + arr[x-1]
            
        return missing+arr[-1]