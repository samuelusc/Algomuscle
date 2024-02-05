class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if len(stack)>1 and char in '+-*/':
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if char == '+':
                    stack.append(num1 + num2)
                elif char == '-':
                    stack.append(num1 - num2)
                elif char == '/':
                    stack.append(num1 / num2)
                else:
                    stack.append(num1 * num2)
            
            else:
                stack.append(char)

        return int(stack[-1])