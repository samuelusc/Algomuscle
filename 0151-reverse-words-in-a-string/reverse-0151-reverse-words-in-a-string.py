class Solution:
    def reverseWords(self, s: str) -> str:
        #s.strip() remove start and end space
        # split() will remove space in s including start and end
        words = s.split()
        # reverse in place
        words.reverse()
        return ' '.join(words)
