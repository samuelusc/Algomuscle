class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            component = target - nums[i]
            if component in hashmap:
                return [hashmap[component], i]
            hashmap[nums[i]] = i

            