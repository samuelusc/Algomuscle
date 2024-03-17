class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums1 = nums + nums
        res = [-1] * len(nums1)

        stack = [0]

        for i in range(1,len(nums1)):
            while stack and nums1[i] > nums1[stack[-1]]:
                res[stack[-1]] = nums1[i]
                stack.pop()
            
            stack.append(i)
        
        res = res[:len(nums)]
        return res


            
