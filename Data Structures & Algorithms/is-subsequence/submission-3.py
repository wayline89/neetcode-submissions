class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left=0

        for right in range(len(t)):
            if left<len(s) and t[right]==s[left]:
                left+=1
        return len(s)==left