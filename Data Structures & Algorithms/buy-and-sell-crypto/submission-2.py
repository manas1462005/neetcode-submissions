class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro=0
        l=0
        r=1
        while r<len(prices):
            if prices[r]<prices[l]:
                l=r
            else:
                maxpro=max(maxpro,prices[r]-prices[l])
            r+=1
        return maxpro
