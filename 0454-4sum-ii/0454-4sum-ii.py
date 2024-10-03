class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = {}

        for a in nums1:
            for b in nums2:
                hashmap[a+b] = hashmap.get(a+b,0)+1
        
 

        count = 0

        for c in nums3:
            for d in nums4:
                target = -(c+d)
                count += hashmap.get(target, 0)
        
        return count