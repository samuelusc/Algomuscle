class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset = set()
        numSet = set(nums1)

        for num in nums2:
            if num in numSet:
                hashset.add(num)
            
        return list(hashset)
