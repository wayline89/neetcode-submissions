class Solution:
    def maxDifference(self, s: str) -> int:
        res={}
        maxim=0
        minim=float('inf')
        
        for letter in s:
            res[letter]=res.get(letter,0)+1
        
        for num in res.values():
            if num%2!=0: 
                maxim=max(maxim,num)
            else:
                minim=min(minim,num)
        
        return maxim-minim