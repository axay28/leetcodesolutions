from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # Dimensions of the matrix
        rows, cols = len(mat), len(mat[0])
        
        # Step 1: Build the heights array
        heights = [[0] * cols for _ in range(rows)]
        
        # Fill the heights array
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    heights[i][j] = heights[i - 1][j] + 1 if i > 0 else 1
                else:
                    heights[i][j] = 0
        
        # Step 2: Count submatrices row by row using a monotonic stack
        total = 0
        for i in range(rows):
            # Count submatrices for the current row
            total += self.countRowSubmatrices(heights[i])
        
        return total
    
    def countRowSubmatrices(self, heights: List[int]) -> int:
        """Helper function to count submatrices in one row using the heights array."""
        stack = []
        sum_in_row = 0
        total = 0
        
        for j, h in enumerate(heights):
            # Maintain a monotonic stack
            count = 1
            while stack and stack[-1][0] >= h:
                prev_height, prev_count = stack.pop()
                sum_in_row -= prev_height * prev_count
                count += prev_count
            
            # Push the current height and its count to the stack
            stack.append((h, count))
            sum_in_row += h * count
            total += sum_in_row
        
        return total
