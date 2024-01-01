class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashTable = dict()
        res = set()
        for num in nums1:
            
            hashTable[num] = hashTable.get(num, 0) + 1

        for num in nums2:
            if num in hashTable:
                res.add(num)

        return list(res)
                
