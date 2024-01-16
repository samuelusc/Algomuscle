class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 使用Counter计算 {Key: a+b Value: count}
        from collections import Counter
        
        # list comprehension 计算a+b 的数量并生成一个dictionary
        ab_sum = Counter(a+b for a in nums1 for b in nums2)
        
        return sum(ab_sum[-(c+d)]for c in nums3 for d in nums4)
