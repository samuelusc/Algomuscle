class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        min_heap = []
        count = Counter(nums)

        for ele, fre in count.items():
            heappush(min_heap,(fre, ele))

            if len(min_heap) > k:
                heappop(min_heap)

            
        top_k = [ele for fre, ele in min_heap]
        return top_k