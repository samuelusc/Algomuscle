class Solution:
    def reverseWords(self, s: str) -> str:
        text = s.split()

        left, right = 0, len(text)-1
        while left < right:
            text[left],text[right] = text[right],text[left]
            left += 1
            right -= 1
        
        return " ".join(text)

# T：O(n) where n is the length of "s"
# S: O(n) where n is the length of "s"
