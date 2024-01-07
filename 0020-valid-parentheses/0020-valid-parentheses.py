class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # the length cannot be length
        if len(s) % 2 != 0:
            return False

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