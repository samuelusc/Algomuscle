class Solution:
    def calculate(self, s: str) -> int:
        stack = [] #Initialize an empty list to be used as a stack
        operator, res = 1, 0 #Initialize operator to be 1and result  
        index, length = 0, len(s)

        while index < length:
            
            if s[index].isdigit():
                num = 0 
                
                while index < length and s[index].isdigit():
                    num = num * 10 + int(s[index])
                    index += 1
                res += num * operator
                index -= 1
            
            elif s[index] == "+":
                operator = 1
            elif s[index] == "-":
                operator = -1

            elif s[index] == "(":
                stack.append(res)
                stack.append(operator)
                res = 0
                operator = 1
            
            elif s[index] == ")":
                res *= stack.pop()
                res += stack.pop()
            index += 1
        return res



