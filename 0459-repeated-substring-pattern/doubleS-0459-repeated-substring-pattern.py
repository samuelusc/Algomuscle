class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        double_s = s + s
        # Note to check len(double_s) instead of len(s)
        index = double_s.find(s, 1,len(double_s)-1)
        print(index)
        if index > 0:
            return True

        return False
