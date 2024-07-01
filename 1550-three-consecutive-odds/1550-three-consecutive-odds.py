class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0
        for num in arr:
            counter = counter + 1 if num % 2 == 1 else 0
            if counter == 3:
                return True
        return False
