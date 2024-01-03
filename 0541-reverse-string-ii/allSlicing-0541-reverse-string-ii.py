class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Initialize a left pointer to track the start of each 2k segment.
        left = 0


        while left < len(s):

            # Calculate the right boundary for the k characters to be reversed.
            right = left + k
            
            # Reverse the k characters starting from 'left' and ending at 'right'.
            # Concatenate it with the non-reversed parts of the string.
            s = s[:left] + s[left:right][::-1] + s[right:]

            # Move the left pointer forward by 2k to process the next segment.
            left = left + 2 * k
        
        # Return the modified string after processing all segments.
        return s

# T: O(n^2/k) S: O(n)

# each iteration process 2k and run n/2k. at each iteration to process slicing and string will be O(n). In total it's about O(n^2/k)
