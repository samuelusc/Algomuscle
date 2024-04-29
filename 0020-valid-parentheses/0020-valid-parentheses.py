class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char not in hashmap:
                stack.append(char)

            elif not stack or hashmap[char]!= stack[-1]:
                return False
            else:
                stack.pop()
        return not stack
            