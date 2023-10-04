#User function Template for python3

class Solution:
    def printSquare(self, N):
        for x in range(0,N):
            for y in range(0,N):
                print("*",end=" ")
            print()
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printSquare(N)
# } Driver Code Ends