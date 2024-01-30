class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmap = {}

        for char in s:
            value = hashmap.get(char, 0) + 1
            hashmap[char] = value

        for char in t:
            value = hashmap.get(char, 0) - 1
            hashmap[char] = value

        return all(value == 0 for key, value in hashmap.items())
             
        