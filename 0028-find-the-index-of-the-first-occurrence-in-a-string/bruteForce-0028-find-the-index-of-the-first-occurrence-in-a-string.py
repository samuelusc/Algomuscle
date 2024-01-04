class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len,n_len = len(haystack), len(needle)
        
        # boundary check
        if h_len < n_len:
            return -1
        # iterate through haystack 
        for i in range(0,h_len - n_len + 1):
            
            left,right = i, 0

            # if the letter of haystack is the same as needle
            if haystack[left] == needle[right]:
                while right < n_len:
                                       
                    if haystack[left] != needle[right]:
                        break
                    if right == n_len-1:
                        return i

                    left += 1
                    right += 1
        return -1
