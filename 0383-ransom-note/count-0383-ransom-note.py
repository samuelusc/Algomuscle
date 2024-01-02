class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       
        #Generator Comprehension--check if magazine has enough of each letter
        # all() True if all elements of the iterable are true
        return all(ransomNote.count(char) <= magazine.count(char) for char in set(ransomNote))
