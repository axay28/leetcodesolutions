class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #coins = 1,3
        #amount = 5
        opt=[float("inf")]*(amount+1)
        opt[0]=0
        for coin in coins:
            for x in range(coin,amount+1):
                opt[x]=min(opt[x],opt[x-coin]+1)
        return opt[amount] if opt[amount]!=float("inf") else -1