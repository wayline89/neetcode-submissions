class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]

        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<t:
                indexed=stack.pop()
                res[indexed]=i-indexed
            stack.append(i)
        return res