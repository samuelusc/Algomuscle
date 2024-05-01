class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        count = Counter(nums)
        top_k = [ele for ele, fre in count.most_common(k)]

        return top_k