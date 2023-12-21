class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        one=min(prices)
        prices.remove(one)
        two=min(prices)
        if money>=one+two:
            return money-(one+two)
        
        return money