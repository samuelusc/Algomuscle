class Solution:
    def isValid(self, s: str) -> bool:
        hashset = {"()","[]","{}"}
        stack = []
        
        for char in s:
            if char in "{[(":
                stack.append(char)
            
            elif not stack or stack.pop() + char not in hashset:
                return False
        
        return not stack