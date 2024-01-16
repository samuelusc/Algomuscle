class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char in ransomNote and ransomNote.count(char) <= magazine.count(
                char
            ):
                continue

            else:
                return False

        return True
