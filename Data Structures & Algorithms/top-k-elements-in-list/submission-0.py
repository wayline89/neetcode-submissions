class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            seen[num]=seen.get(num,0)+1
        return sorted(seen, key=seen.get, reverse=True)[:k]
