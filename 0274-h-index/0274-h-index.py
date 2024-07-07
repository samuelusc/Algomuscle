class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for i in range(len(citations) + 1):
            count = sum(c >= i for c in citations)
            if count >= i:
                h = i
        
        return h