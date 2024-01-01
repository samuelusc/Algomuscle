class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s_counter = Counter(s)
        t_counter = Counter(t)

        return s_counter == t_counter