class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxpiles=max(piles)
        left,right=1,maxpiles

        while left<right:
            speed=(left+right)//2

            if self.look(piles,speed)>h:
                left=speed+1
            else:
                right=speed
        return left


    def look(self,piles,speed):
        s=0
        for pile in piles:
            s+=(pile+speed-1)//speed
        return s

    