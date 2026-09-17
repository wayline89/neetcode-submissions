class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive=0
        maxim=0
        for num in nums:
            if num==0:
                consecutive=0
            else: 
                consecutive +=1
                maxim=max(maxim,consecutive)
        return maxim
