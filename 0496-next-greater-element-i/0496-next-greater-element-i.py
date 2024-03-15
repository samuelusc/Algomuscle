class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = [0] 
        hashmap = dict()

        for i in range(len(nums1)):
            hashmap[nums1[i]] = i

        for i in range(1,len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                if nums2[stack[-1]] in hashmap:
                    index = hashmap[nums2[stack[-1]]]
                    res[index] = nums2[i]
                stack.pop()

            stack.append(i)

        return res    

                