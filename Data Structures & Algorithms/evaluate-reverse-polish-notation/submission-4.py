class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                droite, gauche = stack.pop(), stack.pop()
                stack.append(gauche + droite)
            elif c == "-":
                droite, gauche = stack.pop(), stack.pop()
                stack.append(gauche - droite)
            elif c == "*":
                droite, gauche = stack.pop(), stack.pop()
                stack.append(gauche * droite)
            elif c == "/":
                droite, gauche = stack.pop(), stack.pop()
                stack.append(int(gauche / droite))
            else:
                stack.append(int(c))

        return stack[-1]