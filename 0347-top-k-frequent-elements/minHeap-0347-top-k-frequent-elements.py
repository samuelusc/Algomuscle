class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        from heapq import heappush, heappop
        min_heap =[]
        
        # count frequency of each number in nums by Counter
        counts = Counter(nums)

        #Iterate through counts for each pair(number, frequency)
        for num, freq in counts.items():
            # push a pair of tuple into heap
            heappush(min_heap, (freq, num))
            # check if the heap size exceed k
            if len(min_heap) > k:
                heappop(min_heap)
        
        #extract the top k frequency number(index 2) from tuple 
        top_k = [pair[1] for pair in min_heap]

        return top_k
        
