class Solution:
    def nextTable(self, next:List[int], targetStr: str) -> None:
        # Initialize the pointer for the longest prefix that is also a suffix.
        j = 0
        # The first element in the 'next' array is always 0 as a single character
        # doesn't have any proper prefix or suffix.
        next[0] = 0

        # Iterate through the string to fill up the 'next' array.
        for i in range(1, len(targetStr)):
            # If the characters don't match, move the 'j' pointer back accordingly.
            while j > 0 and targetStr[i] != targetStr[j]:
                j = next[j-1]

            # If the characters match, increment 'j' as we've found a longer prefix which is also a suffix.
            if targetStr[i] == targetStr[j]:
                j += 1

            # Update the 'next' array for the current position.
            next[i] = j

    def repeatedSubstringPattern(self, s: str) -> bool:
        # Edge case: if the string length is less than or equal to 1, it can't have a repeating pattern.
        if len(s) <= 1:
            return False

        # Initialize the 'next' array for the KMP algorithm.
        next = [0] * len(s)
        # Fill the 'next' array for the string 's'.
        self.nextTable(next, s)

        # Check if the last element of the 'next' array is not 0 (indicating a repeated segment) and
        # the length of the string is a multiple of the length of the repeated substring.
        if next[-1] != 0 and len(s) % (len(s) - next[-1]) == 0:
            return True  # The string 's' has a repeated substring pattern.

        # If the conditions are not met, then the string doesn't consist of a repeated substring.
        return False
