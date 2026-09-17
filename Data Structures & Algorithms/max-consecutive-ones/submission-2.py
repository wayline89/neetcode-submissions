class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive=0
        maxim=0
        for num in nums:
            consecutive = consecutive +1if num==1 else 0
            maxim=max(maxim,consecutive)
        return maxim
