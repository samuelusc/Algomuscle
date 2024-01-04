class Solution:
    # Initialize
    # Mismatch between prefix and suffix
    # Match between prefix and suffix
    # Update the next table
    def nextTable(self, next: List[int], s: str)->None:
        # Initialize
        j = 0 # Index for the prefix 
        next[0] = 0  # Base case for the first character
        for i in range(1, len(s)): # i is the index for the suffix
            while j > 0 and s[i] != s[j]:  # While there's a mismatch
                j = next[j-1]  # Fall back in the pattern
            if s[i] == s[j]:  # When there's a match
                j += 1  # Move forward in the pattern
            next[i] = j  # Update the next table at position i


    def strStr(self, haystack: str, needle: str) -> int:
        hay_len, nee_len = len(haystack), len(needle)
        # Boundary check
        if nee_len == 0:
            return 0  # Empty needle always matches at the first position
        if hay_len < nee_len:
            return -1  # Needle longer than haystack means no match
        # Initialize
        next = [0] * nee_len  # Next table for the needle
        self.nextTable(next, needle)  # Build the next table for needle
        j = 0  # Index for needle
        for i in range(hay_len):  # Iterate through haystack
            while j > 0 and haystack[i] != needle[j]:  # Mismatch handling
                j = next[j-1]  # Use next table to avoid unnecessary comparisons
            
            if haystack[i] == needle[j]:  # Match found
                j += 1  # Move to the next character in needle
            
            if j == nee_len:  # Full needle found in haystack
                return i - nee_len + 1  # Return the start index of the match
        
        return -1  # No match found
