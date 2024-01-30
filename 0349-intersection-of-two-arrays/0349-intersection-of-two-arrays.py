class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        res = set()
        for num in nums1:
            hashmap[num] = hashmap.get(num, 0) + 1

        for num in nums2:
            if num in hashmap:
                res.add(num)


        return list(res)