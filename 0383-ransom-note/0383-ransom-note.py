class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        hash_table = Counter(ransomNote)
        
        for i in magazine:
            if i in hash_table:
                hash_table[i] -=1
        # Apply Generator Expression instead of for loop
        # count = sum(1 for count in hash_table.values() if count > 0)

        for count in hash_table.values():
            if count > 0:
                return False
        
        return True
        
            