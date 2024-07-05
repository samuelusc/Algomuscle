class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if nums[i] > 0:
                return res
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1

            while left < right:
                sumTwo = nums[left] + nums[right]
                if sumTwo < -nums[i]:
                    left += 1
                elif sumTwo > -nums[i]:
                    right -= 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
            
        return res    