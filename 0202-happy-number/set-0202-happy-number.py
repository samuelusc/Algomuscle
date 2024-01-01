class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!= 1:
            # calculate by list comprehension
            n = sum(int(i) ** 2 for i in str(n))
            # check if it is in hash table 
            if n in seen:
                return False
            else:
                seen.add(n)
        # if n == 1
        return True
