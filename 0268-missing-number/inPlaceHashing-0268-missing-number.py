class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(len(nums)):
            while nums[i]<n and nums[i]!= nums[nums[i]]:
                #should consider why to apply this order instead of 
                # nums[i],nums[nums[i]]
                nums[nums[i]],nums[i] = nums[i], nums[nums[i]]

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        
        return len(nums)
