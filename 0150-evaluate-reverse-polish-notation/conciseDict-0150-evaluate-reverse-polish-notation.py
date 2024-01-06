#consider both solution 1 and 2 to update solution3
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # refer to solution2 lambda x,y: int(x/y) to update dictionary 
        operators = {'+': lambda x,y : x + y,'-': lambda x,y : x - y ,'*': lambda x,y : x * y, '/': lambda x,y : int(x/y) }
        for token in tokens:
            if token in operators:
                stack[-2] = operators[token](stack[-2],stack[-1])
                stack.pop()
            else:
                stack.append(int(token))
        
        return stack[-1]
