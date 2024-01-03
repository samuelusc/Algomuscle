class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        text = list(s)

        for i in range(0, len(text), 2*k):

            #reverse first k 
            #eventhough the lenght of remaining elements is less than k 
            text[i:i+k] = reversed(text[i: i+k])
        
        return "".join(text)