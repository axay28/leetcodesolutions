class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        if len(prices)<2:
            return money
        heapq.heapify(prices)
        one=heapq.heappop(prices)
        two=heapq.heappop(prices)
        if money >= one + two:
            return money - (one + two)
        
        return money