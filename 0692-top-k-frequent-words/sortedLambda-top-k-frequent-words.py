from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counts = Counter(words)
        # sort each unique word by frequncy in descending,then alphabetically
        top_k = sorted(counts, key = lambda word: (-counts[word] , word))
        # return the first k element by slicing [:k]
        return top_k[:k]
