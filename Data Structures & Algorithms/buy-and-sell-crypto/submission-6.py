class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=float("inf")
        res=0
        for i in range(len(prices)):
            minimum=min(minimum,prices[i])
            res= max(res,prices[i]-minimum)
        return res
