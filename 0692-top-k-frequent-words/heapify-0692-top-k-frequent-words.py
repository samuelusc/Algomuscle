from collections import Counter
from heapq import heapify,heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
       
       counts = Counter(words)
       # negative freq can be used for build up max heap 
       heap = [(-freq, word) for word,freq in counts.items()]
       #heapify the list into a min heap
       # implementing -freq it will work as max heap
       heapify(heap)
       #extract word from tuple(-frequency, word)
       return [heappop(heap)[1] for _ in range(k)]

       
