class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l, r = 0, 1
        maxp = 0
        while r<len(prices):
            if prices[r] - prices[l] < 0:
                l = r
            else:
                maxp = max(maxp, prices[r] - prices[l])
            r+=1
        return maxp