class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        # 使用 Counter 计算每个 num 出现个数
        counts = Counter(nums)
        # 获取出现最多的k个元素
        # most_common() 返回元组，需要解包
        top_k = [element for element,count in counts.most_common(k)]

        return top_k
