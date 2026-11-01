class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        for c in tokens:
            if c=="+":
                prem=stack.pop()
                deux=stack.pop()
                stack.append(deux+prem)
            elif c=="-":
                prem=stack.pop()
                deux=stack.pop()
                stack.append(deux-prem)
            elif c=="*":
                prem=stack.pop()
                deux=stack.pop()
                stack.append(deux*prem)
            elif c=="/":
                prem=stack.pop()
                deux=stack.pop()
                stack.append(int(deux/prem))
            else:
                stack.append(int(c))
        return int(stack[-1])