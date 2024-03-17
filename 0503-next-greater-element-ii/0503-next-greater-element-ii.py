class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = [0]

        for i in range(1,len(nums)):            
            while stack and nums[i] > nums[stack[-1]]:
                res[stack[-1]] =  nums[i]
                stack.pop()
            
            stack.append(i)

        print(f"res: {res} and stack:{stack}")

        if len(stack) > 1:
            for i in range(len(nums)):
                while stack and nums[i] > nums[stack[-1]]:
                    res[stack[-1]] = nums[i]
                    stack.pop()
                    if len(stack) == 1:
                        return res


        return res
