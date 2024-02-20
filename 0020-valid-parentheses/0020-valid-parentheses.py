class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(")")
            
            elif s[i] == '[':
                stack.append("]")
            
            elif s[i] == '{':
                stack.append("}")
            
            elif stack and s[i] == stack[-1]:
                    stack.pop()
            
            else:
                return False
        
        return not stack
            