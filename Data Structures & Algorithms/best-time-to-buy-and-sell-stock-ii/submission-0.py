class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        nbuy=nsell=0
        cbuy=csell=0
        for i in range(n-1,-1,-1):
            cbuy=max(nbuy,-prices[i]+nsell)
            csell=max(nsell,prices[i]+nbuy)
            nbuy=cbuy
            nsell=csell
        return cbuy