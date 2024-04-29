class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack[-2]+= stack[-1]
            
            elif token == "-":
                stack[-2]-= stack[-1]
            
            elif token == "*":
                stack[-2] *= stack[-1]

            elif token == "/":
                stack[-2] = int(stack[-2]/stack[-1])
            
            else:
                stack.append(int(token))
                continue
            stack.pop()
        
        return stack[-1]