class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        hashmap = {}
        for i in nums1:
            for j in nums2:
                hashmap[i+j]= hashmap.get(i+j, 0) + 1

        count = 0
        for x in nums3:
            for y in nums4:
                count += hashmap.get(-(x+y), 0)
        
        return count