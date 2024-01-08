from collections import Counter
from heapq import heapify,heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
       
       counts = Counter(words)
        
       # Create a heap of tuples. Each tuple contains the negative frequency and the word.
       # Using negative frequency turns the min-heap into a max-heap.
       heap = [(-freq, word) for word,freq in counts.items()]
        
       # Convert the list into a heap (in-place).
       # The negative frequency ensures that the heap behaves like a max-heap.
       heapify(heap)
        
       # Pop the top k elements from the heap and return their words.
       # heappop returns the smallest item from the heap (highest frequency due to negative values).
       return [heappop(heap)[1] for _ in range(k)]

       
