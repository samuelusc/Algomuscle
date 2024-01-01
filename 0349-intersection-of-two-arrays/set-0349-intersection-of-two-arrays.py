class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create a set copy of nums1 and nums2
        # find the intersection by & operator
        return list(set(nums1) & set(nums2))
