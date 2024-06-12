class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = "+"
        num = 0

        for index, char in enumerate(s):
            if char.isdigit():
                num = num *10 + int(char)
            
            if char in "+-*/" or index == len(s)-1:
                if sign == "+":
                    stack.append(num)
                
                elif sign == "-":
                    stack.append(-num)
                
                elif sign == "*":
                    stack[-1] *= num
                
                elif sign == "/":
                    stack[-1] = int(stack[-1] / num)
            
                num = 0
                sign = char
            
        return sum(stack)