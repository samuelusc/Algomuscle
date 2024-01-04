class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # boundary check
        h_len,n_len = len(haystack), len(needle)
        
        if h_len < n_len:
            return -1
        
        for i in range(0,h_len - n_len + 1):
            
            left,right = i, 0

            if haystack[left] == needle[right]:
                while right < n_len:
                                       
                    if haystack[left] != needle[right]:
                        break
                    if right == n_len-1:
                        return i

                    left += 1
                    right += 1
        return -1
