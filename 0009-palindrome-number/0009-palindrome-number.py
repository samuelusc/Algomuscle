class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x and x % 10 == 0):
            return False

        half = 0

        while half < x:
            half = half * 10 + x % 10
            x = x // 10

        return x in (half, half // 10)