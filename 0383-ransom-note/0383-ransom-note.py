class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       
        #dictionary appraoch

        hashmap = {}

        for letter in magazine:
            if letter in hashmap:
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1
        
        for letter in ransomNote:
            if letter not in hashmap or hashmap[letter] <= 0:
                return False
            hashmap[letter] -= 1
        return True