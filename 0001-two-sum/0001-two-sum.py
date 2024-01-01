class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        # enumerate throught the list of numbers
        for index, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], index]
            
            seen[num] = index

