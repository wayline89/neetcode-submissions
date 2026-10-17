class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,res=0,0
        vu=set()
        for right in range(len(s)):
            while s[right] in vu:
                vu.remove(s[left])
                left+=1
            vu.add(s[right])
            res=max(res,right-left+1)
        return res
            