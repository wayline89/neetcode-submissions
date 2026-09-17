class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size= len(strs)
        strs.sort()
        if size==0:
            return ""
        if size==1:
            return strs[0]
        
        mot_min=min(len(strs[0]),len(strs[-1]))

        i=0
        while i< mot_min and strs[0][i]== strs[-1][i]:
            i+=1
        return strs[0][0:i]