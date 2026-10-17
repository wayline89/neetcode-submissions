class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,res=0,0
        vus=set()

        for right in range(len(s)):
            while s[right]in vus:
                vus.remove(s[left])
                left+=1
            vus.add(s[right])
            res=max(res,right-left+1)
        return res