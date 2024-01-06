class Solution:
    def isValid(self, s: str) -> bool:
        # Set each pair of parentheses as an element of the set
        hashset = {'()', '{}', '[]'}
        stack = []

        # Handling the case of encountering a left parenthesis
        # Handling the case of encountering a right parenthesis (no left parenthesis in the stack, or the left and right parentheses do not match)
        for char in s:
            # Treat these three types of left parentheses as iterable objects to confirm, and insert them into the stack without commas
            if char in '({[':
                stack.append(char)
            # If the stack is empty or the left and right parentheses do not match, return False
            elif not stack or stack.pop() + char not in hashset:
                return False
        
        # Return True if the stack is empty
        return not stack
