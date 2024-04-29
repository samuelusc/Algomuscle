class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                stack.append(")")
            
            elif char == "[":
                stack.append("]")
            
            elif char == "{":
                stack.append("}")

            elif not stack or char != stack[-1]:
                return False
            else:
                stack.pop()
        
        return not stack