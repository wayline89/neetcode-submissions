class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        ns=s.rstrip()
        
        for i in range(len(ns)):
            if s[i].isspace():
                count=0
                continue
            count+=1
        return count