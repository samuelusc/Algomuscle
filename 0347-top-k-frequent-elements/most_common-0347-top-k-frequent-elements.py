class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        # Use Counter to count the occurrence of each number in nums
        counts = Counter(nums)
        # Retrieve the top k most frequent elements
        # most_common() returns a list of tuples, unpacking them here
        top_k = [element for element, count in counts.most_common(k)]

        return top_k
