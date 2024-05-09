class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <=0:
            return False

        quotient =  n
        reminder  = 0

        while quotient != 1:
            remainder = quotient % 2
            if remainder != 0:
                return False

            quotient = quotient // 2
        
        return True