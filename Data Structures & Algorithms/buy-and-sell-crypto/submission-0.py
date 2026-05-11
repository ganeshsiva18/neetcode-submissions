class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]
        for num in prices:
            maxP = max(maxP, num-minBuy)
            minBuy = min(minBuy, num)
        return maxP