class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums.sort()
        
        # Iterate through the array, leaving 2 elements for the two pointers.
        # E.g., for length = 5 (indexes: 0,1,2,3,4), only iterate through index 2 (0,1,2).
        for i in range(len(nums)-2):
            # As the array is sorted, no three numbers can sum to zero beyond this point.
            if nums[i] > 0: 
                return res
            
            # Skip the same element to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) -1

            while left < right:
                current = nums[i] + nums[left] + nums[right] 
                
                # Check the sum and adjust the pointers accordingly.
                if current > 0:
                    right -= 1
                elif current < 0:
                    left += 1

                else: 
                    res.append([nums[i],nums[left],nums[right]])
                    
                    # Move both pointers for the next potential search.
                    left, right = left + 1, right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res

        # Time Complexity: sort() -> O(nlogn) + nested loop -> n^2 , then it's O(n^2) 
        # Space Complexity : in place sort -> O(1) + output-> n^2 then it's O(n^2)
# If we consider the output space, the worst-case space complexity can be O(n^2) in the scenario where almost all elements are distinct, 
# leading to a quadratic number of valid triplets.
