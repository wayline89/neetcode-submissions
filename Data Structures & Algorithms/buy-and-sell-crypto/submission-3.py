class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        minimum=float('inf')
        for i ,num in enumerate(prices,1):
            minimum=min(minimum,num)
            res= max(res,num-minimum)
        return res