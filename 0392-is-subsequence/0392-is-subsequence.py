class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        if len(s) > len(t):
            return False

        if not s:
            return True
            
        for char in t:
            
            if char == s[s_pointer]:
                s_pointer += 1

            if s_pointer == len(s):
                return True

        return False

            
            
