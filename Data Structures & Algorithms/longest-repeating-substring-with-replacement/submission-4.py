class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,res=0,0
        vu={}

        for right in range(len(s)):
            vu[s[right]]=vu.get(s[right],0)+1
            while right-left+1 - max(vu.values())>k:
                vu[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
        return res

        