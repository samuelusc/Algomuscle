class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        # Subtracting Counters will only retain positive counts
        # and remove negative and zero counts
        return not Counter(ransomNote) - Counter(magazine)