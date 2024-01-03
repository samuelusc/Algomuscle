class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            # create new string and assign to s
            return s[::-1]
        
        elif len(s) < 2*k:
            return s[:k][::-1] + s[k:]

        # convert string to list  
        s = list(s)
        for i in range(0,len(s), 2*k):
                            
            # If the remaining characters are less than k, reverse them and return the string
            if len(s) - i < k:
                
                # Use join() to convert the list back to a string
                return "".join(s[:i] + s[i:][::-1])
            # Reverse the next k characters in place
            s[i:i+k] = s[i:i+k][::-1]
        
        return "".join(s)
# In Python, when you slice a string with an index that is beyond the string's actual length, 
# Python will not throw an error. Instead, it will adapt to the situation and return as many characters as possible.
