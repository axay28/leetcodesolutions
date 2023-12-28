class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []

        for candy in candies: 
            if (extraCandies + candy) >= max(candies):
                answer.append(True)
            else: 
                answer.append(False)

        return answer